import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('viewer_gate', Path(__file__).resolve().parents[1] / 'build/verify_viewer_assets.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class ViewerReleaseGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        viewer = self.root / gate.VIEWER
        native = viewer / 'src-tauri'
        native.mkdir(parents=True)
        for path, content in {
            viewer / 'package.json': {'version': '1.4.0'},
            viewer / 'package-lock.json': {'version': '1.4.0', 'packages': {'': {'version': '1.4.0'}}},
            native / 'tauri.conf.json': {'version': '1.4.0'},
        }.items():
            path.write_text(json.dumps(content))
        (native / 'Cargo.toml').write_text('[package]\nversion = "1.4.0"\n')
        (native / 'Cargo.lock').write_text('[[package]]\nname = "scoville-plan-viewer"\nversion = "1.4.0"\n')
        self.assets = self.root / 'assets'
        self.assets.mkdir()
        self.names = [f'scoville-plan-viewer-v1.4.0-{suffix}' for suffix in gate.SUFFIXES]
        for name in self.names:
            (self.assets / name).write_bytes(name.encode())
        sums = ''.join(f'{hashlib.sha256(name.encode()).hexdigest()}  {name}\n' for name in self.names)
        (self.assets / 'SHA256SUMS.txt').write_text(sums)
        (self.assets / 'BUILD.json').write_text('{}')

    def test_complete_current_inventory_passes(self):
        version, names, sums = gate.local_assets(self.root, self.assets)
        self.assertEqual(version, '1.4.0')
        self.assertEqual(names, set(self.names))
        self.assertEqual(len(sums), 11)

    def test_mutated_binary_is_rejected(self):
        (self.assets / self.names[0]).write_bytes(b'wrong source build')
        with self.assertRaisesRegex(ValueError, 'checksum-mismatched'):
            gate.local_assets(self.root, self.assets)

    def test_mixed_version_owner_is_rejected(self):
        (self.root / gate.VIEWER / 'src-tauri/Cargo.toml').write_text('[package]\nversion = "1.3.3"\n')
        with self.assertRaisesRegex(ValueError, 'version owners must agree'):
            gate.local_assets(self.root, self.assets)

    def test_extra_old_binary_is_rejected(self):
        (self.assets / 'scoville-plan-viewer-v1.3.3-windows-x64.exe').write_bytes(b'old')
        with self.assertRaisesRegex(ValueError, 'extra='):
            gate.local_assets(self.root, self.assets)

    def test_duplicate_checksum_is_rejected(self):
        path = self.assets / 'SHA256SUMS.txt'
        path.write_text(path.read_text() + path.read_text().splitlines()[0] + '\n')
        with self.assertRaisesRegex(ValueError, 'unique basenames'):
            gate.local_assets(self.root, self.assets)

    def test_partial_release_set_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'exactly one --release for Plan'):
            gate.verify(self.root, self.assets, ['benjaminstelzer/scoville-plan=v1.11.0'])

    def attachment(self):
        path = self.assets / self.names[0]
        return path, {'name': path.name, 'state': 'uploaded',
                      'size': path.stat().st_size, 'digest': 'sha256:' + gate.digest(path)}

    def test_uploaded_metadata_matches_approved_file(self):
        path, asset = self.attachment()
        gate.verify_attachment(asset, path)

    def test_wrong_uploaded_digest_is_rejected(self):
        path, asset = self.attachment()
        asset['digest'] = 'sha256:' + '0' * 64
        with self.assertRaisesRegex(ValueError, 'metadata differs'):
            gate.verify_attachment(asset, path)

    def test_missing_uploaded_digest_is_rejected(self):
        path, asset = self.attachment()
        asset.pop('digest')
        with self.assertRaisesRegex(ValueError, 'metadata differs'):
            gate.verify_attachment(asset, path)

    def test_incomplete_upload_is_rejected(self):
        path, asset = self.attachment()
        asset['state'] = 'starter'
        with self.assertRaisesRegex(ValueError, 'metadata differs'):
            gate.verify_attachment(asset, path)


if __name__ == '__main__':
    unittest.main()
