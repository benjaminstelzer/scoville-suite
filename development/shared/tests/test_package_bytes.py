import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'build'))
from build_suite import package_bytes


class PackageBytesTests(unittest.TestCase):
    def test_text_is_checkout_independent_and_binary_is_exact(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in ('SKILL.md', 'helper.py', 'config.json', 'openai.yaml',
                         'icon.svg', 'LICENSE', '.gitattributes'):
                path = Path(directory) / name
                path.write_bytes(b'first\r\nsecond\r\n')
                self.assertEqual(b'first\nsecond\n', package_bytes(path))
                path.write_bytes(b'first\nsecond\n')
                self.assertEqual(b'first\nsecond\n', package_bytes(path))
            for name in ('image.png', 'font.woff2', 'unknown.bin'):
                path = Path(directory) / name
                data = b'\x00\xff\r\n'
                path.write_bytes(data)
                self.assertEqual(data, package_bytes(path))


if __name__ == '__main__':
    unittest.main()
