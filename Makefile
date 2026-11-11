# isort . && black . && bandit -r . && pylint && pre-commit run --all-files
# Get changed files

FILES := $(wildcard **/*.py)

# if you wrap everything in pipenv run, it runs slower.
ifeq ($(origin VIRTUAL_ENV),undefined)
    VENV := poetry run
else
    VENV :=
endif



clean-pyc:  
	@echo "Removing compiled files"
	@find . -name '*.pyc' -exec rm -f {} + || true
	@find . -name '*.pyo' -exec rm -f {} + || true
	@find . -name '__pycache__' -exec rm -fr {} + || true

clean-test:
	@echo "Removing coverage data"
	@rm -f .coverage || true
	@rm -f .coverage.* || true

clean: clean-pyc clean-test

# tests can't be expected to pass if dependencies aren't installed.
# tests are often slow and linting is fast, so run tests on linted code.
test: clean .build_history/pylint .build_history/bandit
	@echo "Running unit tests"
	export FORCE_COLOR=true
	# $(VENV) pytest terminaltables3 --doctest-modules
	# $(VENV) python -m unittest discover
    # not all tests run in all OSs, giving seemingly low coverage.
	FORCE_COLOR=true $(VENV) py.test tests --cov=terminaltables3 --cov-branch --cov-report=html --cov-fail-under 75

.build_history:
	@mkdir -p .build_history

.build_history/isort: .build_history $(FILES)
	@echo "Formatting imports"
	$(VENV) isort terminaltables3
	@touch .build_history/isort

.PHONY: isort
isort: .build_history/isort

.build_history/black: .build_history .build_history/isort $(FILES)
	@echo "Formatting code"
	$(VENV) black . --exclude .virtualenv --exclude .tox
	@touch .build_history/black

.PHONY: black
black: .build_history/black

.build_history/pre-commit: .build_history .build_history/isort .build_history/black
	@echo "Pre-commit checks"
	$(VENV) pre-commit run --all-files
	@touch .build_history/pre-commit

.PHONY: pre-commit
pre-commit: .build_history/pre-commit

.build_history/bandit: .build_history $(FILES)
	@echo "Security checks"
	$(VENV)  bandit .
	@touch .build_history/bandit

.PHONY: bandit
bandit: .build_history/bandit

.PHONY: pylint
.build_history/pylint: .build_history .build_history/isort .build_history/black $(FILES)
	@echo "Linting with pylint"
	# TODO lint tests
	$(VENV) pylint terminaltables3 --fail-under 10
	@touch .build_history/pylint

.PHONY: ruff
.build_history/ruff: .build_history .build_history/isort .build_history/black $(FILES)
	@echo "Linting with ruff"
	$(VENV) ruff check terminaltables3 tests --fix
	@touch .build_history/ruff

.PHONY: ruff
ruff: .build_history/ruff

# for when using -j (jobs, run in parallel)
.NOTPARALLEL: .build_history/isort .build_history/black

check: test pylint ruff bandit pre-commit

.PHONY: publish
publish: check
	rm -rf dist && poetry build

.PHONY: build
build: check
	rm -rf dist && poetry build

.PHONY: mypy
mypy:
	$(VENV) mypy terminaltables3 --ignore-missing-imports --check-untyped-defs
