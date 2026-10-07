import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from test_validate_profile import FIXTURE, SCRIPT, tree_snapshot

CORPUS = Path(__file__).with_name('mojibake-corpus.json')


class MojibakeTests(unittest.TestCase):
    def invoke(self, text, newline='\n', invalid=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'project'
            shutil.copytree(FIXTURE, root)
            path = root / 'docs/plans/0001-validate-profile.md'
            content = path.read_text(encoding='utf-8').replace('Observe one valid profile.', text)
            if invalid:
                content = content.replace('1. Read the canonical files.', '1. [status: paused] Read the canonical files.')
            path.write_bytes(content.replace('\n', newline).encode('utf-8'))
            before = tree_snapshot(root)
            result = subprocess.run([sys.executable, str(SCRIPT), '--root', str(root), '--format', 'json'], capture_output=True)
            self.assertEqual(before, tree_snapshot(root))
            return result.returncode, json.loads(result.stdout), content

    def test_frozen_corpus_quantifies_detection_and_false_alarms(self):
        self.assertEqual(hashlib.sha256(CORPUS.read_bytes()).hexdigest(), 'ef23ab330e887bcc88653eeb69cde5b08a6a551609fd748b7f66196c12a45f0b')
        corpus = json.loads(CORPUS.read_text(encoding='utf-8'))
        negatives_warned, positives_warned = 0, 0
        for kind in ('negative', 'positive'):
            for entry in corpus[kind]:
                with self.subTest(case=entry['id']):
                    status, payload, _ = self.invoke(entry['text'])
                    self.assertEqual(status, 0, payload)
                    self.assertTrue(payload['valid'])
                    self.assertEqual(payload['summary']['errors'], 0)
                    warnings = [d for d in payload['diagnostics'] if d['code'] == 'FILE_MOJIBAKE_SUSPECTED']
                    self.assertEqual(bool(warnings), entry['expected_warning'])
                    self.assertTrue(all(d['severity'] == 'warning' for d in warnings))
                    if warnings:
                        if kind == 'negative': negatives_warned += 1
                        else: positives_warned += 1
        self.assertEqual((positives_warned, negatives_warned), (8, 1))
        self.assertEqual(len(corpus['negative']), 35)

    def test_precise_location_crlf_and_actual_json_consumer(self):
        for newline in ('\n', '\r\n'):
            status, payload, content = self.invoke('Correct ü text.\nDamaged Ã¤ text.', newline)
            self.assertEqual(status, 0, payload)
            warning = next(d for d in payload['diagnostics'] if d['code'] == 'FILE_MOJIBAKE_SUSPECTED')
            self.assertEqual(warning['file'], 'docs/plans/0001-validate-profile.md')
            self.assertEqual(warning['line'], content[:content.index('Ã¤')].count('\n') + 1)
            self.assertEqual(warning['observed'], 'column 9: Ã¤')
            self.assertEqual(payload['summary']['warnings'], 1)
            corrected, clean, _ = self.invoke('Correct ü text.\nDamaged ä text.', newline)
            self.assertEqual(corrected, 0, clean)
            self.assertEqual(clean['summary']['warnings'], 0)

    def test_warning_never_hides_real_syntax_error(self):
        status, payload, _ = self.invoke('Damaged Ã¤ text.', invalid=True)
        self.assertEqual(status, 1)
        self.assertFalse(payload['valid'])
        self.assertGreater(payload['summary']['errors'], 0)
        self.assertEqual(payload['summary']['warnings'], 1)

    def test_escaped_ticks_paragraph_boundaries_and_valid_multiline_spans(self):
        for text, warned in [(r'\`Ã¤\`', True),
                             ('`unfinished\n\nDamaged Ã¤ text.\n\n`later`', True),
                             ('`unfinished\n \t\nDamaged Ã¤ text.\n\n`later`', True),
                             ('`first\nÃ¤\nlast`', False),
                             (r'\\`Ã¤`', False),
                             (r'``inline \` Ã¤``', False),
                             (r'`Ã¤\`', False),
                             (r'\``Ã¤`', False),
                             ('`unfinished\n## Damaged Ã¤ heading\n`later`', True)]:
            with self.subTest(text=text):
                status, payload, _ = self.invoke(text)
                # Extra H2 in this Plan fixture correctly remains a syntax
                # error; it must still surface its independent prose warning.
                self.assertEqual(status, 1 if '\n## ' in text else 0, payload)
                if '\n## ' in text:
                    self.assertIn('SECTION_H2_ORDER', [d['code'] for d in payload['diagnostics']])
                self.assertEqual(bool(payload['summary']['warnings']), warned)


if __name__ == '__main__':
    unittest.main()
