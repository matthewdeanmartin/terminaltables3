# What is it

Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.

Tested on Python 3.9+

**This is a fork of the terminaltables project. Which is archived and unmaintained. This library is in a new namespace
but should otherwise be a drop in replacement. Maintaining goals consist of maintaining ecosystem compatibility, type
annotations and responding to community pull requests.**

To Upgrade
==========
Replace all instances of `terminaltables` with `terminaltables3` in your code. If other libraries depend on `terminaltables`
in your venv they will not conflict because it is a new namespace.

As of right now, the documentation as the robpol86 version.

📖 Full documentation: https://robpol86.github.io/terminaltables

Quickstart
==========

Install:

```bash
pip install terminaltables3
```

Usage:

```python
from terminaltables3 import AsciiTable

table_data = [
    ["Heading1", "Heading2"],
    ["row1 column1", "row1 column2"],
    ["row2 column1", "row2 column2"],
    ["row3 column1", "row3 column2"],
]
table = AsciiTable(table_data)
print
table.table
```

```bash
+--------------+--------------+
| Heading1     | Heading2     |
+--------------+--------------+
| row1 column1 | row1 column2 |
| row2 column1 | row2 column2 |
| row3 column1 | row3 column2 |
+--------------+--------------+
```

Example Implementations
=======================
![Example Scripts Screenshot](https://github.com/matthewdeanmartin/terminaltables/blob/master/docs/examples.png?raw=true)

Source code for examples:

- [example1.py](https://github.com/matthewdeanmartin/terminaltables/blob/master/example1.py)
- [example2.py](https://github.com/matthewdeanmartin/terminaltables/blob/master/example2.py)
- [example3.py](https://github.com/matthewdeanmartin/terminaltables/blob/master/example3.py)

[Change Log](https://github.com/matthewdeanmartin/terminaltables/blob/master/CHANGELOG.md)

## Run tests on Linux locally

With Docker Desktop running:

```sh
docker build -f Dockerfile.test -t terminaltables3-tests .
docker run --rm terminaltables3-tests
```

The image uses Debian slim with Python 3.12 and runs the full quality gate.

## Local development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run:

```sh
uv sync --frozen
make check
```

`make check` runs the same full quality gates as the Python 3.12 Linux job in
GitHub Actions and the GitLab quality job. The other GitHub Actions jobs run
`make test`'s pytest command on the remaining Python and operating system
combinations. Run `make` to list all available targets.
