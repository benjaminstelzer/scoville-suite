"""Actual reader execution against singleton and transport-loss regressions."""
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
READER = ROOT / 'scoville-design-anti-ai-slop/scripts/read-source.py'
spec = importlib.util.spec_from_file_location(
    'reader_coverage', ROOT / 'development/scripts/read_coverage.py')
coverage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coverage)


class SourceReaderTests(unittest.TestCase):
    def run_reader(self, path, *args):
        return subprocess.run([sys.executable, '-B', str(READER), str(path), *args],
                              capture_output=True, encoding='utf-8')

    def test_singleton_blank_crlf_bom_and_empty_preserve_source(self):
        cases = [b'Complete one-line brief', b'Complete one-line brief\n',
                 'Größe\r\n\r\nZeile drei\r\n'.encode(),
                 b'\xef\xbb\xbfOne line with BOM\r\n', b'']
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'source with spaces.txt'
            for source in cases:
                with self.subTest(source=source):
                    path.write_bytes(source)
                    result = self.run_reader(path)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    proof = coverage.verify_coverage([result.stdout], path.as_uri(), source)
                    self.assertTrue(proof['complete'], proof)
                    self.assertIn(f'BYTES={len(source)} SHA256={hashlib.sha256(source).hexdigest()}', result.stdout)
                    self.assertNotIn('COMPLETE', result.stdout)

    def test_actual_381_line_reads_recover_only_received_intervals(self):
        source = ''.join(f'Full source line {i}\n' for i in range(1, 382)).encode()
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'lesson.txt'
            path.write_bytes(source)
            full = self.run_reader(path).stdout
            # Synthetic tool transport loss retains the genuine emitted footer.
            # A footer must never turn the missing middle into received evidence.
            cut = full[:full.index('274: ')] + full[full.index('312: '):]
            incomplete = coverage.verify_coverage([cut], path.as_uri(), source)
            self.assertEqual(incomplete['missing_ranges'], [[274, 311]])
            self.assertFalse(incomplete['complete'])
            recovery = self.run_reader(path, '--start', '273', '--end', '312')
            self.assertEqual(recovery.returncode, 0)
            complete = coverage.verify_coverage([cut, recovery.stdout], path.as_uri(), source)
            self.assertTrue(complete['complete'], complete)

    def test_invalid_or_unavailable_input_never_emits_a_receipt(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'source.txt'
            path.write_bytes(b'One line')
            for args in [('--start', '2'), ('--start', '0'), ('--end', '2'),
                         ('--start', '1', '--end', '0')]:
                with self.subTest(args=args):
                    result = self.run_reader(path, *args)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, '')
            path.write_bytes(b'\xff\xfe\x00')
            result = self.run_reader(path)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, '')
            result = self.run_reader(Path(folder) / 'absent.txt')
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
