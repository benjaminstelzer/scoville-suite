"""Exercise the maintained generators against the single published source."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

DEVELOPMENT = Path(__file__).resolve().parents[1]
REPOSITORY = DEVELOPMENT.parent
PACKAGE = REPOSITORY / 'scoville-design-anti-ai-slop'


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


class CanonicalPackageTests(unittest.TestCase):
    def command(self, script, *args, expected=0):
        result = subprocess.run([sys.executable, '-B', str(DEVELOPMENT/'scripts'/script), *map(str, args)],
                                capture_output=True, text=True, cwd=REPOSITORY)
        self.assertEqual(expected, result.returncode, result.stdout + result.stderr)
        return result

    def test_default_index_and_export_use_single_source_without_modifying_it(self):
        before = snapshot(PACKAGE)
        self.command('generate_module_index.py')
        self.command('generate_module_index.py', '--check')
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            manifest = temporary/'manifest.json'
            self.command('build_package_manifest.py', '--output', manifest)
            self.command('build_package_manifest.py', '--output', manifest, '--check')
            self.command('build_runtime_package.py', '--destination', temporary/'export',
                         '--receipt', temporary/'receipt.json')
            self.assertEqual(before, snapshot(temporary/'export'))
            receipt = json.loads((temporary/'receipt.json').read_text())
            self.assertEqual(receipt['source'], receipt['runtime'])
            rejected = REPOSITORY/'forbidden-second-package'
            self.command('build_runtime_package.py', '--destination', rejected,
                         '--receipt', temporary/'rejected.json', expected=1)
            self.assertFalse(rejected.exists())
        self.assertEqual(before, snapshot(PACKAGE))
        self.assertFalse((REPOSITORY/'SKILL.md').exists())

    def test_index_drift_fails_then_generator_repairs_only_the_index(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)/'package'
            shutil.copytree(PACKAGE, package)
            before = snapshot(package)
            index = package/'references'/'direct-expert-index.md'
            text = index.read_text(encoding='utf-8')
            start = text.index('<!-- MODULE_INDEX:START -->')
            changed = text[:start] + text[start:].replace('→', 'BROKEN', 1)
            self.assertNotEqual(text, changed)
            index.write_text(changed, encoding='utf-8', newline='\n')
            self.command('generate_module_index.py', '--root', package, '--check', expected=1)
            self.command('generate_module_index.py', '--root', package)
            self.assertEqual(before, snapshot(package))
            manifest = Path(directory)/'manifest.json'
            self.command('build_package_manifest.py', '--root', package, '--output', manifest)
            skill = package/'SKILL.md'
            skill.write_text(skill.read_text(encoding='utf-8')+'\nDrift.\n', encoding='utf-8', newline='\n')
            self.command('build_package_manifest.py', '--root', package, '--output', manifest, '--check', expected=1)

    def test_repeated_groups_require_internal_and_outside_anchor_dispositions(self):
        core = " ".join((PACKAGE / "SKILL.md").read_text(encoding="utf-8").split())
        composition = " ".join(
            (PACKAGE / "references/composition-and-layout.md")
            .read_text(encoding="utf-8").split()
        )
        self.assertIn("check internal rhythm and both external anchors", core)
        self.assertIn(
            "internal gaps and both outside endpoints",
            composition,
        )
        self.assertIn("Equal gaps for equal outside anchors", composition)

    def test_authored_static_state_sequences_keep_motion_ownership(self):
        motion = " ".join(
            (PACKAGE / "references/motion-and-sequence.md")
            .read_text(encoding="utf-8").split()
        )
        registry = (PACKAGE / "modules.yaml").read_text(encoding="utf-8")
        self.assertIn("A sequence of authored still states selects this module", motion)
        self.assertIn("already independent still images with no state/continuity relation", motion)
        self.assertIn("authored state sequence or storyboard", registry)


    def test_specialists_carry_declared_local_correctness_checks(self):
        expected = {
            'advertising-and-campaign-art-direction.md': 'button-shaped carrier as an action only when an action exists',
            'information-design-and-data-visualization.md': 'derive the affine map from at least two known',
            'physical-wayfinding-and-signage-systems.md': 'enumerate each route segment where it approaches or',
            'instructional-and-explanatory-design.md': 'make a transition\nledger before styling',
            'packaging-graphics-and-sku-systems.md': 'use painted fill and stroke edges',
            'motion-and-sequence.md': 'both outside endpoints against any shared span',
        }
        for filename, phrase in expected.items():
            with self.subTest(filename=filename):
                text = (PACKAGE / 'references' / filename).read_text(encoding='utf-8')
                self.assertIn(phrase, text)


if __name__ == '__main__':
    unittest.main()
