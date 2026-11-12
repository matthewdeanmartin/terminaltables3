# Contributing

Everyone that wants to contribute to the project should read this document.

## Getting Started

You may follow these steps if you wish to create a pull request. Fork the repo and clone it on your local machine. Then
in the project's directory:

```bash
uv sync --frozen
make check
```

Run tests with a specific Python version using `uv run --python 3.9 --frozen pytest tests`.
The CI matrix covers Python 3.9, 3.12, and 3.15 on Linux and the low and high
versions on macOS and Windows.

## Preparing a Release

1. Add user-visible changes under `Unreleased` in `CHANGELOG.md`.
2. Each push to `master` refreshes the draft GitHub Release from `Unreleased`.
   Review the draft's version and notes, then publish it from the current
   `master` commit.
3. Publishing runs `build.yml`: `kaclm release-bump` updates the changelog,
   `pyproject.toml`, and `terminaltables3.__version__`, then opens a release
   pull request. The workflow builds and publishes from that bumped branch.
4. Merge the release pull request after the PyPI publish succeeds.

## Updating Docs

Documentation lives in `docs/` and can be edited directly. Build it with:

```bash
make docs
```

The HTML output is written to `docs/_build/html`.

## Consistency and Style

Keep code style consistent with the rest of the project. Some suggestions:

1. **Write tests for your new features and for bug fixes.**
2. Write docstrings for all classes, functions, methods, modules, etc.
3. Document all function/method arguments and return values.
4. Document all class variables instance variables.
5. Documentation guidelines also apply to tests, though not as strict.
6. Keep code style consistent, such as the kind of quotes to use and spacing.
7. Don't use `except:` or `except Exception:` unless you have a `raise` in the block. Be specific about error handling.
8. Don't use `isinstance()` (it breaks [duck typing](https://en.wikipedia.org/wiki/Duck_typing#In_Python)).

## Thanks

Thanks for fixing bugs or adding features to the project!
