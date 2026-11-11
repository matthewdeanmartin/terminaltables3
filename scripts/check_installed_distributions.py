"""Install each built artifact outside the checkout and verify its public API."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SMOKE_TEST = """
from importlib.metadata import version
from pathlib import Path
import sys

import terminaltables3
from terminaltables3 import (
    AsciiTable, DoubleTable, GithubFlavoredMarkdownTable, PorcelainTable, SingleTable
)

installed = Path(terminaltables3.__file__).resolve()
try:
    installed.relative_to(Path(sys.prefix).resolve())
except ValueError:
    raise AssertionError(f"Imported from outside the fresh environment: {installed}")

assert version("terminaltables3") == terminaltables3.__version__
rows = [["Name", "Value"], ["alpha", "1"]]
for table_type in (
    AsciiTable, DoubleTable, GithubFlavoredMarkdownTable, PorcelainTable, SingleTable
):
    rendered = table_type(rows).table
    assert "Name" in rendered and "alpha" in rendered, table_type.__name__
"""


def run(*args, cwd, env):
    subprocess.run(args, cwd=cwd, env=env, check=True)


def check_artifact(artifact, root):
    name = "wheel" if artifact.suffix == ".whl" else "sdist"
    work = root / name
    work.mkdir()
    venv = work / "venv"
    python = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    run("uv", "venv", "--python", sys.executable, str(venv), cwd=work, env=env)
    run(
        "uv",
        "pip",
        "install",
        "--python",
        str(python),
        "--no-deps",
        str(artifact),
        cwd=work,
        env=env,
    )
    run(str(python), "-I", "-c", SMOKE_TEST, cwd=work, env=env)
    print("Installed artifact passed:", artifact.name)


def main():
    wheels = sorted(DIST.glob("*.whl"))
    sdists = sorted(DIST.glob("*.tar.gz"))
    if len(wheels) != 1 or len(sdists) != 1:
        raise SystemExit("Expected exactly one wheel and one sdist in dist/")
    with tempfile.TemporaryDirectory(prefix="terminaltables3-artifacts-") as temp:
        for artifact in (wheels[0], sdists[0]):
            check_artifact(artifact.resolve(), Path(temp))


if __name__ == "__main__":
    main()
