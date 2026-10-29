import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'build'))
from build_suite import package_bytes, payload, render_readmes
import build_suite as builder


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


    def test_shared_provenance_hashes_normalized_bytes_but_manifest_identifies_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root, shared = Path(directory) / 'suite', Path(directory) / 'shared'
            root.mkdir()
            paths = {'readme/license.md': b'License.\n',
                     'prompting/common.md': b'Writing.\n{{ include: rules.native_output }}\n',
                     'runtime/native_output.md': b'Native capture.\n',
                     'runtime/skill_optout.md': b'Opt out.\n',
                     'runtime/skill_composition.md': b'Composition.\n'}
            (root / 'skill.md').write_bytes(b'# Example\n{{ include: rules.optout }}\n')
            config = {'schema_version': 1, 'name': 'fixture', 'profile': 'codex',
                      'repository': 'benjaminstelzer/fixture', 'readme': [],
                      'members': [{'name': 'example', 'repository': 'benjaminstelzer/example',
                                   'visibility': 'public', 'public_distribution': True,
                                   'readme': ['shared:license.md'],
                                   'files': [{'source': 'skill.md', 'target': 'example/SKILL.md'},
                                             {'source': 'shared:prompting/common.md',
                                              'target': 'example/references/writing.md'}]}]}
            manifest = (json.dumps(config, indent=2) + '\n').encode()
            receipts = []
            for label, newline in (('lf', b'\n'), ('crlf', b'\r\n')):
                for name, data in paths.items():
                    target = shared / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data.replace(b'\n', newline))
                (root / 'suite.json').write_bytes(manifest.replace(b'\n', newline))
                with patch.object(builder, 'shared_root', return_value=shared), \
                        patch.object(builder.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '', '')):
                    receipt = builder.build(root, Path(directory) / label, True, [])
                self.assertEqual(hashlib.sha256((root / 'suite.json').read_bytes()).hexdigest(),
                                 receipt['manifest_sha256'])
                for name, data in paths.items():
                    self.assertEqual(hashlib.sha256(data).hexdigest(), receipt['shared_sources'][name])
                receipts.append(receipt)
            self.assertEqual(receipts[0]['shared_sources'], receipts[1]['shared_sources'])
            self.assertNotEqual(receipts[0]['manifest_sha256'], receipts[1]['manifest_sha256'])

    def test_payload_and_readme_expansion_normalize_crlf(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'intro.md').write_bytes(b'# Example\r\n\r\nREADME text.\r\n')
            (root / 'SKILL.md').write_bytes(b'---\r\nname: example\r\ndescription: Example.\r\n---\r\n\r\n{{ include: family.contract }}\r\n\r\n{{ include: helper.policy }}\r\n')
            member = {'name': 'example', 'readme': ['intro.md'],
                      'files': [{'source': 'SKILL.md', 'target': 'example/SKILL.md'},
                                {'source': 'shared:runtime/task_lifecycle.py',
                                 'target': 'example/scripts/task_lifecycle.py'}],
                      'helper_contracts': {'scripts/task_lifecycle.py': {'kind': 'helper'}}}
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
