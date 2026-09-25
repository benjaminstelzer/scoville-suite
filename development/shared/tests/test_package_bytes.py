import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'build'))
from build_suite import package_bytes, payload, render_readmes


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


    def test_payload_and_readme_expansion_normalize_crlf(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'intro.md').write_bytes(b'# Example\r\n\r\nREADME text.\r\n')
            (root / 'SKILL.md').write_bytes(b'---\r\nname: example\r\ndescription: Example.\r\n---\r\n\r\n{{ include: family.contract }}\r\n')
            member = {'name': 'example', 'readme': ['intro.md'],
                      'files': [{'source': 'SKILL.md', 'target': 'example/SKILL.md'}],
                      'shared_helpers': [{'source': 'runtime/task_lifecycle.py',
                                          'target': 'example/scripts/task_lifecycle.py'}]}
            config = {'name': 'fixture', 'layout': 'suite', 'members': [member], 'readme': ['intro.md']}
            files = payload(root, member, config)
            self.assertIn(b'installed and enabled', files['example/SKILL.md'])
            for name, data in files.items():
                self.assertNotIn(b'\r', data, name)
            render_readmes(root, True, config)
            self.assertNotIn(b'\r', (root / 'README.md').read_bytes())
            self.assertNotIn(b'\r', (root / 'members/example/README.md').read_bytes())


if __name__ == '__main__':
    unittest.main()
