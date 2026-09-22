"""Own a CLI process tree until verified shutdown.

Adapted for Scoville Suite development from the local, user-owned
``gemini-worker/scripts/worker_process.py`` helper. That source repository has
no standalone LICENSE file. This copy is the canonical dependency for the
suite's Codex CLI evaluation runner; it has no runtime dependency on another
workspace repository.
"""

from __future__ import annotations

import os
from pathlib import Path
import signal
import subprocess
import sys
import time


if os.name == "nt":
    import ctypes
    from ctypes import wintypes

    class BasicLimits(ctypes.Structure):
        _fields_ = [
            ("PerProcessUserTimeLimit", ctypes.c_longlong),
            ("PerJobUserTimeLimit", ctypes.c_longlong),
            ("LimitFlags", wintypes.DWORD),
            ("MinimumWorkingSetSize", ctypes.c_size_t),
            ("MaximumWorkingSetSize", ctypes.c_size_t),
            ("ActiveProcessLimit", wintypes.DWORD),
            ("Affinity", ctypes.c_size_t),
            ("PriorityClass", wintypes.DWORD),
            ("SchedulingClass", wintypes.DWORD),
        ]

    class IoCounters(ctypes.Structure):
        _fields_ = [
            (name, ctypes.c_ulonglong)
            for name in (
                "ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
                "ReadTransferCount", "WriteTransferCount", "OtherTransferCount",
            )
        ]

    class ExtendedLimits(ctypes.Structure):
        _fields_ = [
            ("BasicLimitInformation", BasicLimits),
            ("IoInfo", IoCounters),
            ("ProcessMemoryLimit", ctypes.c_size_t),
            ("JobMemoryLimit", ctypes.c_size_t),
            ("PeakProcessMemoryUsed", ctypes.c_size_t),
            ("PeakJobMemoryUsed", ctypes.c_size_t),
        ]

    class Accounting(ctypes.Structure):
        _fields_ = [
            (name, ctypes.c_longlong)
            for name in (
                "TotalUserTime", "TotalKernelTime", "ThisPeriodTotalUserTime",
                "ThisPeriodTotalKernelTime",
            )
        ] + [
            (name, wintypes.DWORD)
            for name in (
                "TotalPageFaultCount", "TotalProcesses", "ActiveProcesses",
                "TotalTerminatedProcesses",
            )
        ]

    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    for name, args, result in (
        ("CreateJobObjectW", [ctypes.c_void_p, wintypes.LPCWSTR], wintypes.HANDLE),
        ("SetInformationJobObject", [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD], wintypes.BOOL),
        ("QueryInformationJobObject", [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD, ctypes.c_void_p], wintypes.BOOL),
        ("OpenProcess", [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD], wintypes.HANDLE),
        ("AssignProcessToJobObject", [wintypes.HANDLE, wintypes.HANDLE], wintypes.BOOL),
        ("TerminateJobObject", [wintypes.HANDLE, wintypes.UINT], wintypes.BOOL),
        ("CloseHandle", [wintypes.HANDLE], wintypes.BOOL),
    ):
        function = getattr(kernel, name)
        function.argtypes = args
        function.restype = result

    def checked(result):
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return result

    class WindowsJob:
        def __init__(self):
            self.handle = checked(kernel.CreateJobObjectW(None, None))
            try:
                limits = ExtendedLimits()
                limits.BasicLimitInformation.LimitFlags = 0x2000
                checked(kernel.SetInformationJobObject(
                    self.handle, 9, ctypes.byref(limits), ctypes.sizeof(limits)
                ))
            except BaseException:
                self.close()
                raise

        def assign(self, pid):
            handle = checked(kernel.OpenProcess(0x101, False, pid))
            try:
                checked(kernel.AssignProcessToJobObject(self.handle, handle))
            finally:
                kernel.CloseHandle(handle)

        def terminate(self):
            checked(kernel.TerminateJobObject(self.handle, 1))
            deadline = time.monotonic() + 10
            while True:
                info = Accounting()
                checked(kernel.QueryInformationJobObject(
                    self.handle, 1, ctypes.byref(info), ctypes.sizeof(info), None
                ))
                if not info.ActiveProcesses:
                    return
                if time.monotonic() >= deadline:
                    raise OSError("Worker job did not become empty within ten seconds")
                time.sleep(0.02)

        def close(self):
            if self.handle:
                checked(kernel.CloseHandle(self.handle))
                self.handle = None


class WorkerProcess:
    def __init__(self, command, **kwargs):
        self.job = None
        self.process = None
        try:
            if os.name == "nt":
                self.job = WindowsJob()
                command = [sys.executable, str(Path(__file__).resolve()), "--launch", *command]
                kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
            else:
                kwargs["start_new_session"] = True
            self.process = subprocess.Popen(command, **kwargs)
            if self.job:
                self.job.assign(self.process.pid)
        except BaseException:
            try:
                if self.process:
                    self.process.kill()
                    self.process.wait(timeout=10)
                    if self.process.stdin:
                        self.process.stdin.close()
            finally:
                if self.job:
                    self.job.close()
            raise

    @property
    def pid(self):
        return self.process.pid

    @property
    def returncode(self):
        return self.process.returncode

    def communicate(self, input, timeout):
        if self.job:
            input = b"\0" + input
        return self.process.communicate(input=input, timeout=timeout)

    def close(self):
        try:
            if self.job:
                self.job.terminate()
            else:
                try:
                    os.killpg(self.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            self.process.wait(timeout=10)
        finally:
            if self.job:
                self.job.close()
            if self.process.stdin and not self.process.stdin.closed:
                self.process.stdin.close()


def launch_after_assignment(command):
    if os.read(sys.stdin.fileno(), 1) != b"\0":
        return 125
    try:
        return subprocess.Popen(
            command,
            stdin=sys.stdin.buffer,
            stdout=sys.stdout.buffer,
            stderr=sys.stderr.buffer,
        ).wait()
    except OSError:
        print("Cannot launch the worker executable.", file=sys.stderr)
        return 125


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "--launch":
        raise SystemExit("Internal worker launcher; invoke run_codex_cli_case.py instead.")
    raise SystemExit(launch_after_assignment(sys.argv[2:]))
