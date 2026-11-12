.DEFAULT_GOAL := help
UV := uv
RUN := $(UV) run --frozen

.PHONY: help sync clean-pyc clean-test clean test isort black format-check pre-commit bandit pylint ruff mypy docs build dist-check artifact-check changelog-check check

help:
	@echo "Available commands:"
	@echo "  help             List all Makefile commands (default)"
	@echo "  sync             Install dependencies from uv.lock"
	@echo "  clean-pyc        Remove Python bytecode and __pycache__ directories"
	@echo "  clean-test       Remove coverage data"
	@echo "  clean            Run clean-pyc and clean-test"
	@echo "  test             Run unit tests with branch coverage"
	@echo "  isort            Format imports"
	@echo "  black            Format Python code"
	@echo "  format-check     Check Black and isort formatting"
	@echo "  pre-commit       Run all pre-commit hooks"
	@echo "  bandit           Run security checks on the package"
	@echo "  pylint           Run pylint on the package"
	@echo "  ruff             Run essential Ruff checks"
	@echo "  mypy             Run static type checks"
	@echo "  docs             Build the Sphinx documentation"
	@echo "  build            Build and validate sdist and wheel"
	@echo "  dist-check       Check built metadata and wheel contents"
	@echo "  artifact-check   Install and smoke-test the wheel and sdist"
	@echo "  changelog-check  Validate the changelog with kaclm"
	@echo "  check            Run the same quality gates as GitHub Actions"

sync:
	$(UV) sync --frozen

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -f .coverage .coverage.*

clean: clean-pyc clean-test

test:
	$(RUN) pytest tests --cov=terminaltables3 --cov-branch --cov-report=term-missing --cov-fail-under=95

isort:
	$(RUN) python -X utf8 -m isort terminaltables3 tests scripts

black:
	$(RUN) black terminaltables3 tests scripts

format-check:
	$(RUN) python -X utf8 -m isort --check-only terminaltables3 tests scripts
	$(RUN) black --check terminaltables3 tests scripts

pre-commit:
	$(RUN) pre-commit run --all-files

bandit:
	$(RUN) bandit -q -r terminaltables3

pylint:
	$(RUN) pylint terminaltables3 --fail-under 10

ruff:
	$(RUN) ruff check terminaltables3 tests scripts --select E4,E7,E9,F

mypy:
	$(RUN) mypy terminaltables3 --ignore-missing-imports --check-untyped-defs

docs:
	$(UV) run --frozen --group docs sphinx-build -W -b html docs docs/_build/html

build:
	$(UV) build --no-sources
	@"$(MAKE)" dist-check
	@"$(MAKE)" artifact-check

dist-check:
	$(UV) run --with 'twine>=7' twine check --strict dist/*
	$(RUN) check-wheel-contents dist/*.whl

artifact-check:
	$(RUN) python scripts/check_installed_distributions.py

changelog-check:
	$(UV) tool run --from keepachangelog-manager-fork kaclm validate

check: format-check test ruff bandit pylint mypy build changelog-check
