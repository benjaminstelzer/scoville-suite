"""Real builder + lifecycle, in-memory adapter, mock host. No native dispatch."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import test_contract as contract
from test_contract import PROMPT_BUILDER, ROOT

class DispatchTransportTests(unittest.TestCase):
    def test_builder_binding_and_transport(self):
        context = contract.NativeWorkflowContractTests.dispatch_context("W-003/step-2", ["2. Preserve äöü 😀 and md:w-1/2."])
        with tempfile.TemporaryDirectory() as tmp:
            selector = Path(tmp) / "selector.py"
            selector.write_text("import os\nprint(os.environ['FAKE_PLAN_CONTEXT'])\n", encoding="utf-8")
            command = [sys.executable, "-B", str(PROMPT_BUILDER),
                "--selector", str(selector), "--plan-root", str(ROOT),
                "--unit", "W-003/step-2", "--role", "executor",
                "--workspace-root", str(ROOT), "--return-to-thread-id", "coordinator",
                "--recipient-model", "gpt-6-sol", "--delivery-reference", "test-reference", "--guard-workflow-id", "test-workflow",
                "--guard-generation", "1", "--guard-revision", "7",
                "--guard-dispatch-key", "test-dispatch", "--guard-task-id", "test-writer"]
            env = {**os.environ, "FAKE_PLAN_CONTEXT": json.dumps(context)}
            def run(extra, input="{}", environment=env):
                p = subprocess.run(command + extra, input=input, env=environment,
                    text=True, encoding="utf-8", capture_output=True)
                self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
                return p.stdout
            envelope = json.loads(run(["--transport-json", "--transport-target", "test-writer"]))
            self.assertEqual(envelope["prompt"], run([]))
            self.assertEqual(envelope["receipt"]["sha256"],
                hashlib.sha256(envelope["prompt"].encode()).hexdigest())
            self.assertEqual(envelope["binding"], json.loads(run(["--binding-only"]))["binding"])
            changed = json.loads(json.dumps(context))
            changed["work_item"]["outcome"] = "Changed outcome"
            other = {**env, "FAKE_PLAN_CONTEXT": json.dumps(changed)}
            self.assertNotEqual(envelope["binding"],
                json.loads(run(["--binding-only"], environment=other))["binding"])
            profile_file = contract.PACKAGE / "references/prompting/medium.md"
            original_profile = profile_file.read_bytes()
            try:
                profile_file.write_bytes(original_profile + b"\nKeep the requested result explicit.\n")
                self.assertNotEqual(envelope["binding"], json.loads(run(["--binding-only"]))["binding"])
            finally:
                profile_file.write_bytes(original_profile)
            p = subprocess.run(["node", str(Path(__file__).with_name("test_dispatch_transport.cjs")),
                str(PROMPT_BUILDER.with_name("dispatch_transport.js")),
                str(ROOT.parents[2] / "shared/runtime/task_lifecycle.py"), sys.executable],
                input=json.dumps(envelope), text=True, encoding="utf-8", capture_output=True)
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
            self.assertIn("transport cases passed", p.stdout)

if __name__ == "__main__":
    unittest.main()
