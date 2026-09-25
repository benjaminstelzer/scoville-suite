import copy
import sys
import unittest
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scoville-workflow-for-codex" / "scripts"))
from check_context_checkpoint import decide as decide_configured, read_thresholds
from inspect_native_context import InspectionError


def decide(sample, identity, role="coordinator"):
    return decide_configured(sample, identity, role, {"coordinator_percent": 33, "worker_percent": 66})


def events(used=33000):
    return [
        {"ordinal": 0, "type": "session_meta", "payload": {"session_id": "coordinator"}},
        {"ordinal": 1, "type": "turn_context", "payload": {"turn_id": "turn"}},
        {"ordinal": 2, "type": "event_msg", "payload": {"type": "token_count", "info": {
            "last_token_usage": {"input_tokens": used},
            "total_token_usage": {"input_tokens": 54000000},
            "model_context_window": 100000,
        }}},
    ]


class CoordinatorContextTests(unittest.TestCase):
    def test_imported_defaults_and_fresh_post_compaction_sample(self):
        from test_contract import PACKAGE
        thresholds = read_thresholds(PACKAGE / 'assets/workflow.toml', PACKAGE)
        self.assertEqual(thresholds, {'coordinator_percent': 25, 'worker_percent': 75})
        for role, used, expected in [('coordinator', 24999, 'continue'),
                                    ('coordinator', 25000, 'rollover'),
                                    ('executor', 75000, 'continue'),
                                    ('executor', 75001, 'context_handoff'),
                                    ('reviewer', 75001, 'context_handoff'),
                                    ('repair', 75001, 'context_handoff')]:
            self.assertEqual(expected, decide_configured(events(used), 'coordinator', role, thresholds)['action'])
        sample = events(80000)
        sample.append({'ordinal': 3, 'type': 'compacted', 'payload': {}})
        sample.append(copy.deepcopy(sample[1]) | {'ordinal': 4})
        sample.append(copy.deepcopy(events(10000)[-1]) | {'ordinal': 5})
        self.assertEqual('continue', decide_configured(sample, 'coordinator', 'executor', thresholds)['action'])

    def test_configured_thresholds_and_invalid_configuration(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "workflow.toml"
            path.write_text('schema_version = 1\n[context]\ncoordinator_percent = 40\nworker_percent = 70\n')
            config = read_thresholds(path)
            for role, used, expected in [("coordinator", 39999, "continue"), ("coordinator", 40000, "rollover"), ("executor", 70000, "continue"), ("executor", 70001, "context_handoff")]:
                self.assertEqual(expected, decide_configured(events(used), "coordinator", role, config)["action"])
            for value in ('true', '0', '100', '33.5', '"33"'):
                path.write_text(f'schema_version = 1\n[context]\ncoordinator_percent = {value}\nworker_percent = 66\n')
                with self.assertRaises(ValueError):
                    read_thresholds(path)
            path.write_text('schema_version = 1\n')
            with self.assertRaises(ValueError):
                read_thresholds(path)

    def test_worker_threshold_is_strict_and_shared_by_roles(self):
        for role in ("executor", "repair", "reviewer"):
            for used, expected in [(33000, "continue"), (65999, "continue"), (66000, "continue"), (66001, "context_handoff")]:
                with self.subTest(role=role, used=used):
                    self.assertEqual(expected, decide(events(used), "coordinator", role)["action"])

    def test_threshold_and_cumulative_usage(self):
        for used, expected in [(32999, "continue"), (33000, "rollover"), (40300, "rollover")]:
            with self.subTest(used=used):
                self.assertEqual(expected, decide(events(used), "coordinator")["action"])

    def test_divi_boundary(self):
        sample = events(104121)
        sample[-1]["payload"]["info"]["model_context_window"] = 258400
        self.assertEqual("rollover", decide(sample, "coordinator")["action"])

    def test_missing_wrong_identity_stale_and_invalid(self):
        cases = [events()[:-1], events()]
        cases[1][0]["payload"]["session_id"] = "worker"
        for kind in ("compacted", "turn_context"):
            case = events()
            case.append({"ordinal": 3, "type": kind, "payload": {"turn_id": "turn"}})
            cases.append(case)
        for value in (None, True, -1, 0, 100001):
            cases.append(events(value))
        terminal = events()
        terminal.append({"ordinal": 3, "type": "event_msg", "payload": {"type": "task_complete", "turn_id": "turn"}})
        cases.append(terminal)
        for case in cases:
            with self.subTest(case=case), self.assertRaises(InspectionError):
                decide(copy.deepcopy(case), "coordinator")


if __name__ == "__main__":
    unittest.main()
