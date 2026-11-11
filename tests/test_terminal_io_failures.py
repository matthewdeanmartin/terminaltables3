"""Failure paths for the Windows console API, independent of host platform."""

import ctypes
import struct
import sys
from types import ModuleType

import pytest

from terminaltables3.terminal_io import (
    get_console_info,
    set_terminal_title,
    terminal_size,
)


class FailingConsole:
    def GetConsoleScreenBufferInfo(self, handle, buffer):
        return 0

    def GetStdHandle(self, handle):
        return 1


def test_console_query_failure_raises_os_error(monkeypatch):
    monkeypatch.setattr(
        ctypes, "WinError", lambda: OSError("console query failed"), raising=False
    )
    with pytest.raises(OSError, match="console query failed"):
        get_console_info(FailingConsole(), 1)


def test_terminal_size_uses_defaults_after_both_console_queries_fail(monkeypatch):
    monkeypatch.setattr("terminaltables3.terminal_io.IS_WINDOWS", True)
    monkeypatch.setattr(
        ctypes, "WinError", lambda: OSError("console query failed"), raising=False
    )
    assert terminal_size(FailingConsole()) == (79, 24)


def test_posix_terminal_size_reads_ioctl_dimensions(monkeypatch):
    monkeypatch.setattr("terminaltables3.terminal_io.IS_WINDOWS", False)
    fcntl = ModuleType("fcntl")
    termios = ModuleType("termios")
    termios.TIOCGWINSZ = 42

    def ioctl(fd, request, buffer):
        assert (fd, request) == (0, 42)
        assert len(buffer) == 8
        return struct.pack("hhhh", 31, 117, 0, 0)

    fcntl.ioctl = ioctl
    monkeypatch.setitem(sys.modules, "fcntl", fcntl)
    monkeypatch.setitem(sys.modules, "termios", termios)
    assert terminal_size() == (117, 31)


@pytest.mark.parametrize("title", ["Café", "Café".encode("utf-8")])
def test_posix_terminal_title_accepts_text_and_bytes(monkeypatch, capsys, title):
    monkeypatch.setattr("terminaltables3.terminal_io.IS_WINDOWS", False)
    assert set_terminal_title(title)
    assert capsys.readouterr().out == "\x1b]0;Café\x07"
