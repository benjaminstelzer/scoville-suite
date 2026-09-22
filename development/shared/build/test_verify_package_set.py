import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from verify_package_set import verify


class PackageSetTests(unittest.TestCase):
    def test_union_and_failures(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            root = base / 'public'
            root.mkdir()
            receipts = []
            for name in ('scoville', 'ask'):
                (root / name).mkdir()
                (root / name / 'SKILL.md').write_bytes(b'contract')
                receipt = base / (name + '.json')
                receipt.write_text(json.dumps({'schema_version': 1, 'suite': name,
                    'members': [{'package_path': name, 'files': {
                        'SKILL.md': hashlib.sha256(b'contract').hexdigest()}}]}))
                receipts.append(receipt)
            self.assertTrue(verify(root, receipts)['valid'])
            (root / 'ask' / 'SKILL.md').write_bytes(b'changed')
            self.assertIn('hash mismatch: ask/SKILL.md', verify(root, receipts)['errors'])
            (root / 'ask' / 'SKILL.md').unlink()
            self.assertIn('missing: ask/SKILL.md', verify(root, receipts)['errors'])
            (root / 'extra').mkdir()
            self.assertIn('extra directory: extra', verify(root, receipts)['errors'])
            with self.assertRaises(ValueError):
                verify(root, receipts + [receipts[0]])
            data = json.loads(receipts[0].read_text())
            data['members'][0]['package_path'] = '../escape'
            receipts[0].write_text(json.dumps(data))
            with self.assertRaises(ValueError):
                verify(root, receipts)


if __name__ == '__main__':
    unittest.main()
