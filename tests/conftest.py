"""Keep tests independent of inherited terminal and color settings."""

import os

import pytest

_original_color_env = None
_color_keys = ("NO_COLOR", "ANSI_COLORS_DISABLED", "FORCE_COLOR")


def pytest_configure(config):
    global _original_color_env
    _original_color_env = {key: os.environ.get(key) for key in _color_keys}
    os.environ.pop("NO_COLOR", None)
    os.environ.pop("ANSI_COLORS_DISABLED", None)
    os.environ["FORCE_COLOR"] = "1"


def pytest_unconfigure(config):
    for key, value in _original_color_env.items():
        if value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = value


@pytest.fixture(autouse=True)
def restore_environment():
    """Prevent one test's environment changes from reaching the next test."""
    before = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(before)
