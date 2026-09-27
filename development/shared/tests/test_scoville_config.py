import importlib.util
from pathlib import Path
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "runtime/scoville_config.py"
SPEC = importlib.util.spec_from_file_location("scoville_config_under_test", SOURCE)
config = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(config)


class ScovilleConfigDiagnosticsTests(unittest.TestCase):
    def test_bad_section_names_path_and_corrected_config_is_read(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            config_path = root / ".scoville/config.json"
            config_path.parent.mkdir()
            config_path.write_text('{"ask": null}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, r"\$\.ask must be an object"):
                config.read_config(root)

            config_path.write_text('{"ask": {"advisers": []}}', encoding="utf-8")
            self.assertEqual(config.section("ask", root), {"advisers": []})
            with self.assertRaisesRegex(ValueError, r"name='claude' .*'ask' or 'workflow'"):
                config.section("claude", root)

    def test_bad_merge_overlay_names_argument_and_corrected_object_merges(self):
        with self.assertRaisesRegex(ValueError, r"overlay must be an object"):
            config.merge({"ask": {}}, [])
        with self.assertRaisesRegex(ValueError, r"base must be an object"):
            config.merge([], {})
        self.assertEqual(config.merge({"ask": {"effort": "high"}},
                                      {"ask": {"effort": "low"}}),
                         {"ask": {"effort": "low"}})

    def test_malformed_json_names_file_and_location_then_valid_read_works(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            config_path = root / ".scoville/config.json"
            config_path.parent.mkdir()
            config_path.write_text('{', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, r"config\.json is invalid JSON at line 1, column"):
                config.read_config(root)
            config_path.write_text('{}', encoding="utf-8")
            self.assertEqual(config.read_config(root), {})


if __name__ == "__main__":
    unittest.main()
