import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
import contextlib
import io


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "development/luna-tests/run_codex_cli_case.py"
sys.path.insert(0, str(RUNNER_PATH.parent))
spec = importlib.util.spec_from_file_location("codex_case", RUNNER_PATH)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


THREAD_ID = "01a0c4a1-43ef-7033-ad98-86f55c057357"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def event_stream(answer="final", thread_id=THREAD_ID):
    events = [
        {"type": "thread.started", "thread_id": thread_id},
        {"type": "item.completed", "item": {"type": "error", "message": runner.KNOWN_CODE_MODE_ERROR}},
        {"type": "turn.started"},
        {"type": "item.completed", "item": {"type": "agent_message", "text": answer}},
        {"type": "turn.completed", "usage": {"input_tokens": 10}},
    ]
    return b"".join((json.dumps(item) + "\n").encode() for item in events)


class RequestContainmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "skill"
        (self.root / "references").mkdir(parents=True)
        self.data = b"line one\r\nline two\r\n"
        (self.root / "references/valid.md").write_bytes(self.data)
        self.manifest = {"references/valid.md": digest(self.data)}

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_manifested_text_is_verified_and_normalized(self):
        delivered, observed = runner.validate_requested_file(
            "references/valid.md", self.root, self.manifest, set()
        )
        self.assertEqual(b"line one\nline two\n", delivered)
        self.assertEqual(digest(self.data), observed)

    def test_rejects_traversal_absolute_backslash_duplicate_and_unmanifested(self):
        invalid = ("references/../valid.md", "/references/valid.md", "C:/x", "references\\valid.md", "references//valid.md", "references/missing.md")
        for relative in invalid:
            with self.subTest(relative=relative), self.assertRaises(runner.ProtocolError):
                runner.validate_requested_file(relative, self.root, self.manifest, set())
        with self.assertRaisesRegex(runner.ProtocolError, "duplicate_request"):
            runner.validate_requested_file("references/valid.md", self.root, self.manifest, {"references/valid.md"})

    def test_rejects_symlinked_file_and_parent(self):
        outside = Path(self.temp.name) / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        file_link = self.root / "references/link.md"
        parent_link = self.root / "assets"
        outside_dir = Path(self.temp.name) / "outside"
        outside_dir.mkdir()
        (outside_dir / "item.md").write_text("outside parent", encoding="utf-8")
        try:
            file_link.symlink_to(outside)
            parent_link.symlink_to(outside_dir, target_is_directory=True)
        except OSError as error:
            self.skipTest(f"symlinks unavailable: {error}")
        manifested = {
            "references/link.md": digest(outside.read_bytes()),
            "assets/item.md": digest((outside_dir / "item.md").read_bytes()),
        }
        for relative in manifested:
            with self.subTest(relative=relative), self.assertRaises(runner.ProtocolError):
                runner.validate_requested_file(relative, self.root, manifested, set())

    def test_read_response_must_be_only_exact_read_lines(self):
        self.assertEqual(["references/a.md"], runner.parse_read_requests("READ references/a.md"))
        with self.assertRaises(runner.ProtocolError):
            runner.parse_read_requests("READ references/a.md\nexplanation")

    def test_receipt_verifies_complete_member_inventory_and_rejects_unsafe_path(self):
        (self.root / "SKILL.md").write_text("core", encoding="utf-8")
        (self.root.parent / "README.md").write_text("readme", encoding="utf-8")
        receipt = self.root.parent / "receipt.json"
        member = {
            "name": "skill", "package_path": "untrusted/not-used",
            "files": {
                "README.md": digest(b"readme"),
                "skill/SKILL.md": digest(b"core"),
                "skill/references/valid.md": digest(self.data),
            },
        }
        receipt.write_text(json.dumps({"members": [member]}), encoding="utf-8")
        self.assertEqual(
            {"SKILL.md", "references/valid.md"},
            set(runner.load_receipt(receipt, "skill", self.root)),
        )
        member["files"]["../escape"] = digest(b"x")
        receipt.write_text(json.dumps({"members": [member]}), encoding="utf-8")
        with self.assertRaises(runner.ProtocolError):
            runner.load_receipt(receipt, "skill", self.root)


class EventContractTests(unittest.TestCase):
    def test_exact_qualified_sequence_passes(self):
        result = runner.validate_events(event_stream(), THREAD_ID)
        self.assertEqual("final", result["answer"])
        self.assertEqual(THREAD_ID, result["thread_id"])

    def test_tool_permission_and_unknown_events_fail(self):
        for event in (
            {"type": "item.started", "item": {"type": "command_execution"}},
            {"type": "permission.requested"},
            {"type": "future.event"},
        ):
            lines = event_stream().splitlines()
            lines[3] = json.dumps(event).encode()
            with self.subTest(event=event["type"]), self.assertRaises(runner.ProtocolError):
                runner.validate_events(b"\n".join(lines) + b"\n", THREAD_ID)

    def test_event_after_turn_completed_fails(self):
        trailing = event_stream() + b'{"type":"future.event"}\n'
        with self.assertRaises(runner.ProtocolError):
            runner.validate_events(trailing, THREAD_ID)


class NativeIdentityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write_rollout(self, name, session_id=THREAD_ID, contexts=None):
        contexts = contexts or [{"model": "gpt-5.6-luna", "effort": "medium"}]
        records = [{"type": "session_meta", "payload": {"id": session_id}}]
        records.extend({"type": "turn_context", "payload": item} for item in contexts)
        path = self.root / name
        path.write_text("\n".join(json.dumps(item) for item in records) + "\n", encoding="utf-8")
        return path

    def test_exact_rollout_and_all_contexts_pass(self):
        self.write_rollout(f"rollout-{THREAD_ID}.jsonl", contexts=[
            {"model": "gpt-5.6-luna", "effort": "medium"},
            {"model": "gpt-5.6-luna", "effort": "medium"},
        ])
        result = runner.validate_native_identity(self.root, THREAD_ID, "gpt-5.6-luna", "medium", 2)
        self.assertEqual(2, len(result["turn_contexts"]))

    def test_missing_ambiguous_and_mismatched_native_identity_fail(self):
        with self.assertRaises(runner.ProtocolError):
            runner.validate_native_identity(self.root, THREAD_ID, "gpt-5.6-luna", "medium", 1)
        self.write_rollout(f"a-{THREAD_ID}.jsonl")
        self.write_rollout(f"b-{THREAD_ID}.jsonl")
        with self.assertRaises(runner.ProtocolError):
            runner.validate_native_identity(self.root, THREAD_ID, "gpt-5.6-luna", "medium", 1)
        for path in self.root.iterdir():
            path.unlink()
        for session_id, contexts in (
            ("wrong", None),
            (THREAD_ID, [{"model": "wrong", "effort": "medium"}]),
            (THREAD_ID, [{"model": "gpt-5.6-luna", "effort": "wrong"}]),
        ):
            self.write_rollout(f"one-{THREAD_ID}.jsonl", session_id, contexts)
            with self.assertRaises(runner.ProtocolError):
                runner.validate_native_identity(self.root, THREAD_ID, "gpt-5.6-luna", "medium", 1)
            (self.root / f"one-{THREAD_ID}.jsonl").unlink()
        path = self.root / f"missing-meta-{THREAD_ID}.jsonl"
        path.write_text(json.dumps({"type": "turn_context", "payload": {"model": "gpt-5.6-luna", "effort": "medium"}}) + "\n", encoding="utf-8")
        with self.assertRaises(runner.ProtocolError):
            runner.validate_native_identity(self.root, THREAD_ID, "gpt-5.6-luna", "medium", 1)


class FailureAndCommandTests(unittest.TestCase):
    def result(self, **changes):
        value = {"stdout": event_stream(), "stderr": b"", "returncode": 0, "timed_out": False, "close_error": None}
        value.update(changes)
        return value

    def test_stderr_timeout_nonzero_parse_close_and_incomplete_fail(self):
        cases = (
            self.result(stderr=b"warning"), self.result(timed_out=True),
            self.result(returncode=2), self.result(stdout=b"not json\n"),
            self.result(close_error="close failed"),
            self.result(stdout=b'{"type":"thread.started","thread_id":"x"}\n'),
            self.result(stdout=event_stream(answer="   ")),
        )
        for index, result in enumerate(cases):
            with self.subTest(index=index), self.assertRaises(runner.ProtocolError):
                runner.validate_process_result(result, None)

    def test_resume_keeps_isolation_flags_and_exact_thread(self):
        base = runner.base_command(Path("codex.exe"), Path("catalog.json"), "gpt-5.6-luna", "medium")
        command = runner.turn_command(base, Path("workspace"), THREAD_ID)
        self.assertEqual(["exec", "resume"], command[len(base):len(base) + 2])
        self.assertEqual([THREAD_ID, "-"], command[-2:])
        for value in ("never", "read-only", "mcp_servers={}", 'web_search="disabled"', "--ignore-user-config", "--ignore-rules", "--strict-config", "--skip-git-repo-check", "--json"):
            self.assertIn(value, command)
        disabled = [command[index + 1] for index, value in enumerate(command[:-1]) if value == "--disable"]
        self.assertEqual(list(runner.DISABLED_FEATURES), disabled)

    def test_terra_medium_is_explicit_and_other_pairs_remain_rejected(self):
        command = runner.base_command(Path("codex.exe"), Path("catalog.json"), "gpt-5.6-terra", "medium")
        self.assertEqual(command[command.index("--model") + 1], "gpt-5.6-terra")
        self.assertIn('model_reasoning_effort="medium"', command)
        for model, effort in (("gpt-5.6-terra", "high"), ("unknown", "medium")):
            with self.assertRaises(runner.ProtocolError):
                runner.base_command(Path("codex.exe"), Path("catalog.json"), model, effort)


class TurnBudgetTests(unittest.TestCase):
    def arguments(self, root):
        args = []
        for name in ('case-id', 'prompt', 'package-root', 'receipt', 'receipt-member', 'catalog', 'codex', 'output'):
            args.extend(('--' + name, str(root / name)))
        args.extend(('--model', 'gpt-5.6-luna', '--effort', 'medium'))
        for name in ('prompt', 'receipt', 'catalog', 'codex'):
            args.extend(('--expected-' + name + '-sha256', 'a' * 64))
        return args

    def test_default_eight_and_explicit_bounds(self):
        args = self.arguments(Path.cwd())
        self.assertEqual(8, runner.parse_args(args).max_turns)
        for value in (1, 4, 8):
            self.assertEqual(value, runner.parse_args(args + ['--max-turns', str(value)]).max_turns)
        for value in (0, 9):
            with self.subTest(value=value), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                runner.parse_args(args + ['--max-turns', str(value)])

    def test_final_after_four_reads_and_exhaustion(self):
        # Exercise the real loop; only process/native I/O and package serving are stubbed.
        for budget, expected_exit, expected_turns in ((8, 0, 5), (4, 1, 4)):
            with self.subTest(budget=budget), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                (root / 'prompt').write_bytes(b'Case')
                calls = []
                def execute(command, prompt, workspace, timeout, thread_id):
                    calls.append(thread_id)
                    answer = f'READ references/{len(calls)}.md' if len(calls) <= 4 else 'Final answer'
                    return dict(stdout=event_stream(answer), stderr=b'', returncode=0,
                                timed_out=False, close_error=None, stream_error=None, worker_pid=1)
                with patch.object(runner, 'verify_hash', return_value='a' * 64), \
                     patch.object(runner, 'load_receipt', return_value={'SKILL.md': 'a' * 64}), \
                     patch.object(runner, 'validate_requested_file', return_value=(b'reference', 'a' * 64)), \
                     patch.object(runner, 'execute_turn', side_effect=execute), \
                     patch.object(runner, 'validate_native_identity', return_value={}), \
                     contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(expected_exit, runner.main(self.arguments(root) + ['--max-turns', str(budget)]))
                result = json.loads((root / 'output/summary.json').read_text(encoding='utf-8'))
                self.assertEqual(expected_turns, result['turn_count'])
                self.assertEqual([None] + [THREAD_ID] * (expected_turns - 1), calls)
                self.assertEqual(None if budget == 8 else 'turn_limit_without_final_answer', result['protocol_failure'])


class ProcessLifetimeIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.workspace = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def run_python(self, source, prompt=b"prompt", timeout=1):
        return runner.execute_turn(
            [sys.executable, "-c", source], prompt, self.workspace, timeout
        )

    def process_is_active(self, pid):
        if os.name != "nt":
            try:
                os.kill(pid, 0)
            except ProcessLookupError:
                return False
            return True
        import ctypes
        handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
        if not handle:
            return False
        try:
            code = ctypes.c_ulong()
            if not ctypes.windll.kernel32.GetExitCodeProcess(handle, ctypes.byref(code)):
                return False
            return code.value == 259
        finally:
            ctypes.windll.kernel32.CloseHandle(handle)

    def test_child_not_reading_stdin_times_out_and_descendant_is_stopped(self):
        pid_file = self.workspace / "child.pid"
        source = (
            "import pathlib,subprocess,sys,time; "
            "child=subprocess.Popen([sys.executable,'-c','import time; time.sleep(60)']); "
            f"pathlib.Path({str(pid_file)!r}).write_text(str(child.pid)); "
            "time.sleep(60)"
        )
        started = time.monotonic()
        result = self.run_python(source, b"x" * (16 * 1024 * 1024), timeout=1)
        self.assertLess(time.monotonic() - started, 6)
        self.assertTrue(result["timed_out"])
        self.assertIsNone(result["close_error"])
        self.assertTrue(pid_file.is_file())
        self.assertFalse(self.process_is_active(int(pid_file.read_text())))

    def test_forbidden_event_aborts_while_child_would_stay_alive(self):
        source = (
            "import json,time; "
            "print(json.dumps({'type':'permission.requested'}),flush=True); "
            "time.sleep(60)"
        )
        started = time.monotonic()
        result = self.run_python(source, timeout=10)
        self.assertLess(time.monotonic() - started, 5)
        self.assertEqual("unexpected_event_order", result["stream_error"])
        self.assertIsNone(result["close_error"])
        self.assertIn(b"permission.requested", result["stdout"])

    def test_stdin_write_failure_still_stops_process_tree(self):
        source = "raise SystemExit(0)"
        started = time.monotonic()
        result = self.run_python(source, b"x" * (16 * 1024 * 1024), timeout=10)
        self.assertLess(time.monotonic() - started, 5)
        self.assertTrue(result["stream_error"].startswith("stdin_write_failure:"))
        self.assertIsNone(result["close_error"])


if __name__ == "__main__":
    unittest.main()
