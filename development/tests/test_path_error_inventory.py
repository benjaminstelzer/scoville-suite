"""Check inventory results, positions and read-only behavior with an actual reader."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'inventory_paths_and_errors.py'


class InventoryTests(unittest.TestCase):
    def invoke(self, root, output):
        return subprocess.run([sys.executable, '-B', str(SCRIPT), '--root',
                               'fixture=' + str(root), '--output-file', str(output)],
                              capture_output=True, text=True, encoding='utf-8')

    def test_real_reader_consumes_positions_hashes_imports_paths_and_errors(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root = base / 'source Ä 中文'
            root.mkdir()
            source = ('from pathlib import Path as P\n'
                      'ä = "value"; p = P("data.csv")\n'
                      'try:\n    p.read_text(encoding="utf-8")\n'
                      'except OSError as error:\n    raise ValueError(str(error))\n'
                      'def call_wrapper(value):\n    return unknown_wrapper(value)\n')
            (root / 'helper.py').write_text(source, encoding='utf-8', newline='\n')
            (root / 'README.md').write_text('[guide](references/guide.md)\n', encoding='utf-8')
            (root / 'component.ts').write_text('import { thing } from "library";\n', encoding='utf-8')
            (root / 'opaque.bin').write_bytes(b'\xff\0\x01')
            (root / 'broken.py').write_text('def unfinished(:\n', encoding='utf-8')
            (root / 'node_modules').mkdir()
            (root / 'node_modules/external.js').write_text('external', encoding='utf-8')
            original = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            output = base / 'inventory.json'
            result = self.invoke(root, output)
            self.assertEqual(result.returncode, 0, result.stderr)
            delivery = json.loads(result.stdout)
            self.assertEqual(Path(delivery['output_file']), output.resolve())
            self.assertEqual(delivery['output_sha256'], hashlib.sha256(output.read_bytes()).hexdigest())
            # Actual downstream JSON reader checks source positions, not implementation constants.
            inventory = json.loads(output.read_text(encoding='utf-8'))
            self.assertEqual(inventory['verdict'], 'unreviewed_candidates')
            metadata = {item['file']: item for item in inventory['files']}
            self.assertEqual(metadata['helper.py']['sha256'], hashlib.sha256(original['helper.py']).hexdigest())
            self.assertEqual(metadata['broken.py']['analysis']['method'], 'python_parse_failed')
            self.assertEqual(metadata['opaque.bin']['analysis']['method'], 'not_parsed')
            self.assertTrue(any(item['file'] == 'node_modules' and item['reason'] for item in inventory['excluded']))
            helper_sites = [item for item in inventory['sites'] if item['file'] == 'helper.py']
            kinds = {item['kind'] for item in helper_sites}
            self.assertTrue({'python_import', 'python_path_operation_candidate', 'python_raise',
                             'python_error_handler', 'python_unclassified_call'} <= kinds)
            for item in helper_sites:
                self.assertEqual(source[item['start_offset']:item['end_offset']], item['matched_text'])
                prefix = source[:item['start_offset']]
                self.assertEqual(item['line'], prefix.count('\n') + 1)
                self.assertEqual(item['column'], len(prefix.rsplit('\n', 1)[-1]) + 1)
                self.assertEqual(source[item['context_start_offset']:item['context_end_offset']], item['context'])
            self.assertTrue(any(item['kind'] == 'import_text_candidate' and item['matched_text'] == 'library'
                                for item in inventory['sites']))
            self.assertTrue(any(item['kind'] == 'markdown_reference' and item['matched_text'] == 'references/guide.md'
                                for item in inventory['sites']))
            again = base / 'again.json'
            self.assertEqual(self.invoke(root, again).returncode, 0)
            self.assertEqual(output.read_bytes(), again.read_bytes())
            self.assertEqual(original, {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()})

    def test_invalid_input_and_output_leave_no_partial_success_then_corrected_reader_works(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root = base / 'source Ä 中文'
            output = base / 'inventory.json'
            missing = self.invoke(root, output)
            self.assertNotEqual(missing.returncode, 0)
            self.assertEqual(missing.stdout, '')
            self.assertIn('--root', missing.stderr)
            self.assertIn(str(root), missing.stderr)
            self.assertFalse(output.exists())
            root.mkdir()
            (root / 'a.py').write_text('from pathlib import Path\n', encoding='utf-8')
            forbidden = self.invoke(root, root / 'inventory.json')
            self.assertNotEqual(forbidden.returncode, 0)
            self.assertEqual(forbidden.stdout, '')
            self.assertIn('--output-file', forbidden.stderr)
            self.assertFalse((root / 'inventory.json').exists())
            corrected = self.invoke(root, output)
            self.assertEqual(corrected.returncode, 0, corrected.stderr)
            self.assertEqual(len(json.loads(output.read_text(encoding='utf-8'))['files']), 1)
            before = output.read_bytes()
            duplicate = self.invoke(root, output)
            self.assertNotEqual(duplicate.returncode, 0)
            self.assertEqual(duplicate.stdout, '')
            self.assertEqual(output.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
