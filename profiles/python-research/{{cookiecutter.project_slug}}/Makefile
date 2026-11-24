BASE_REF ?= refs/remotes/origin/main
export BASE_REF
.DEFAULT_GOAL := check

.PHONY: sync check lint typecheck architecture test test-science regression run

sync:
	uv sync --locked

check: lint typecheck architecture test

lint: sync
	uv run --no-sync ruff check --config pyproject.toml src tests scripts
	uv run --no-sync ruff format --config pyproject.toml --check src tests scripts

typecheck: sync
	uv run --no-sync mypy --config-file pyproject.toml src tests

architecture: sync
	uv run --no-sync lint-imports --no-cache --no-logo pyproject.toml

test: sync
	uv run --no-sync pytest -c pyproject.toml --confcutdir=tests tests/fast

test-science: sync
	uv run --no-sync pytest -c pyproject.toml --confcutdir=tests tests/scientific

regression: sync
	uv run --no-sync python scripts/check_complexity.py
	uv run --no-sync jscpd src --no-gitignore --config .jscpd.json --baseline-from-ref "$$BASE_REF" --fail-on-new-clones 0

run: sync
	uv run --no-sync python -m {{ cookiecutter.package_name }}.pipeline --config models/example/config.toml
