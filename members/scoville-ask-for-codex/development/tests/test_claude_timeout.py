"""Exercise deadline configuration and the actual owned process family."""
import ctypes
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from test_ask_behavior import ask, prepare_request, ADVISERS


class ClaudeTimeoutTests(unittest.TestCase):
    def request(self):
        return ask.prepare(prepare_request([ADVISERS[1]]))["entries"][0]["request"]

    def test_default_override_and_invalid_deadlines(self):
        request = self.request()
        result = subprocess.CompletedProcess([], 0, '{"result":"ok"}', '')
        with mock.patch.object(ask.ask_claude, 'resolve_claude_command', return_value=['fake']), mock.patch.object(ask.ask_claude, 'run_command', return_value=result) as run:
            ask.claude(request)
            self.assertEqual(run.call_args.args[3], 3600)
            ask.claude({**request, 'timeout_seconds': 7200})
            self.assertEqual(run.call_args.args[3], 7200)
            for value in (None, True, 0, -1, '60', float('inf'), float('nan')):
                with self.subTest(value=value), self.assertRaises(ValueError):
                    ask.claude({**request, 'timeout_seconds': value})
        configured = ask.resolve({'overrides': {'advisers': ['fable'], 'claude': {'timeout_seconds': 5400}}})
        self.assertEqual(configured['config']['claude']['timeout_seconds'], 5400)

    def test_timeout_has_stable_error_code(self):
        request = {**self.request(), 'operation': 'claude'}
        with mock.patch.object(sys, 'stdin', io.StringIO(json.dumps(request))), mock.patch.object(sys, 'stdout', io.StringIO()) as output, mock.patch.object(ask.ask_claude, 'resolve_claude_command', return_value=['fake']), mock.patch.object(ask.ask_claude, 'run_command', side_effect=ask.ask_claude.ClaudeTimeout('deadline')) as run:
            self.assertEqual(ask.main(), 1)
            self.assertEqual(json.loads(output.getvalue()), {'ok': False, 'error': 'deadline', 'code': 'claude_timeout'})
            run.assert_called_once()

    @unittest.skipUnless(sys.platform == 'win32', 'Windows process-family integration')
    def test_wrapper_and_child_stop_but_control_survives(self):
        kernel = ctypes.WinDLL('kernel32', use_last_error=True)
        kernel.OpenProcess.argtypes = [ctypes.c_ulong, ctypes.c_int, ctypes.c_ulong]
        kernel.OpenProcess.restype = ctypes.c_void_p
        kernel.CloseHandle.argtypes = [ctypes.c_void_p]
        kernel.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
        def alive(pid):
            handle = kernel.OpenProcess(0x100000, False, pid)
            if not handle:
                return False
            try:
                return kernel.WaitForSingleObject(handle, 0) == 258
            finally:
                kernel.CloseHandle(handle)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            script = root / 'wrapper.py'
            script.write_text("import os, subprocess, sys, time, json\nfrom pathlib import Path\nchild=subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'])\nPath('pids.json').write_text(json.dumps([os.getpid(),child.pid]))\ntime.sleep(60)\n", encoding='utf-8')
            control = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'], creationflags=subprocess.CREATE_NO_WINDOW)
            try:
                with self.assertRaises(ask.ask_claude.ClaudeTimeout) as caught:
                    ask.ask_claude.run_command([sys.executable, str(script)], root, 'question', 2)
                self.assertNotIn('could not be confirmed', str(caught.exception))
                pids = json.loads((root / 'pids.json').read_text())
                self.assertEqual(len(pids), 2)
                for pid in pids:
                    self.assertFalse(alive(pid), f'owned process {pid} survived')
                self.assertIsNone(control.poll())
            finally:
                control.kill()
                control.wait()

if __name__ == '__main__':
    unittest.main()
