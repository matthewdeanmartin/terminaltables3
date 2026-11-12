# Known bugs and follow-ups

Library code under `terminaltables3/` was intentionally not modified. These are proposed fixes for a future change.

## 1. Type annotations describe generators as tuples

`mypy` passes because `terminaltables3/build.py` is untyped, but the public annotations are wrong:

- `terminaltables3/base_table.py:94` — `horizontal_border()` is annotated `-> Tuple[str, ...]`, but it returns the
  generator produced by `combine()`.
- `terminaltables3/base_table.py:143` — `gen_row_lines()` is annotated `Generator[Tuple[str, ...], None, None]`, but
  `build_row()` yields `combine()` generators, not tuples.
- `terminaltables3/base_table.py:209` — `gen_table()` has the same issue.

Add real annotations to `build.py` (for example `Iterator[str]` / `Generator[str, None, None]`) and update the
`BaseTable` signatures so type checkers can validate them.

## 2. `set_terminal_title()` writes to stdout on POSIX

`terminaltables3/terminal_io.py:98` writes the title escape sequence to `sys.stdout`. When stdout is redirected or
piped, the sequence goes into the pipe instead of the terminal. Write to the controlling terminal (for example
`/dev/tty`) or stderr, and handle the failure path.

## 3. Empty tables render degenerate output

`AsciiTable([]).table` returns `'++\n++'` and `AsciiTable([[]]).table` returns `'++\n||\n++'`. Decide whether empty
tables should return `''` (as `PorcelainTable` does) or a documented value, and add regression tests.

## 4. Markdown table border toggles produce invalid Markdown

`GithubFlavoredMarkdownTable` inherits `outer_border` and `inner_column_border`, but its `horizontal_border()`
hardcodes `|`. Setting either toggle to `False` removes pipes from the data rows while the heading separator keeps
them, producing invalid GitHub Flavored Markdown. Either ignore the toggles in `gen_table()` or keep documenting them
as unsupported (the docs currently do the latter).

## 5. Stale module docstring URL

`terminaltables3/__init__.py:5` points at `https://github.com/Robpol86/terminaltables3`, which does not exist. It
should point at `https://github.com/matthewdeanmartin/terminaltables3`. The `__author__` value was updated to include
both maintainers.

## 6. `visible_width()` docstring inaccuracies

`terminaltables3/width_and_alignment.py:15` says CJK characters are "more than one byte"; they occupy two terminal
columns. Line 17 links to a non-existent `Robpol86/terminaltables3` pull request.

## 7. Comment typo

`terminaltables3/other_tables.py:188` says "outer birders"; it should say "outer borders".

## 8. Separator settings missing from class docstrings

The `:ivar:` lists on `BaseTable` and `AsciiTable` omit `inner_separators` and `inner_separators_delimiter`. The user
docs were updated in `docs/settings.rst`, but the generated API docs should list them too.
