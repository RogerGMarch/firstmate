# {{ cookiecutter.project_name }}

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and GNU Make.
The example uses synthetic data and runs without data downloads.

```sh
make check
make run
make test-science
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm {{ cookiecutter.project_slug }}
```

`make check` checks formatting and lint with Ruff, strict types with mypy, dependency direction with Import Linter, and the fast pytest suite.
`make test-science` runs the scientific suite separately and is available through the manual **Scientific validation** workflow.
Keep the committed `uv.lock` current with intentional dependency changes.

## Project layout

- `src/{{ cookiecutter.package_name }}/` owns reusable analysis and the pipeline entry point.
- `tests/fast/` holds small fixtures and `tests/scientific/` holds heavier validation.
- `models/example/config.toml` contains the sample run's resolved inputs.
- `data/`, `notebooks/`, and `reports/figures/` hold local datasets, exploration, and outputs.
- [AGENTS.md](AGENTS.md) links to both research skills.

Record each real dataset's immutable version, access instructions, and provenance alongside the experiment configuration.
Document evaluation splits, expected artifacts, and the command for rerunning each reported result.

## Base comparison

Run `git fetch origin main`, then `make regression`.
Use `make regression BASE_REF=<base-commit>` when reviewing against another accepted revision.
The Git base must exist locally and contain the accepted `src/` tree.
CI uses the PR's base SHA and tests the merge result.

The complexity check compares functions and methods in `src/` by file and qualified name.
It rejects score increases for existing functions and scores above 10 for new functions.
After a rename or move, the new-function ceiling applies.
jscpd rejects new Python clones under `.jscpd.json` using the same settings on both revisions.
Import Linter requires every top-level module to belong to the declared dependency layers.
Existing projects may record narrowly scoped legacy import exceptions in the reviewed contract.

## Firstmate and merge protection

1. Seed the repository's `main` with the reviewed workflow, lockfile, skills, and `.no-mistakes.yaml`.
2. Ensure `.github/CODEOWNERS` lists a real GitHub user or team with write access.
3. In GitHub, require pull requests, a human approval, code-owner approval, and the **Python quality** and **Require no-mistakes** checks on `main`.
   Dismiss stale approvals and limit bypass access to maintainers.
4. Install no-mistakes v1.84.0 or newer and run `no-mistakes init`.
   For fork-based delivery, use the fork initialization procedure. [No-mistakes quick start](https://kunchenguid.github.io/no-mistakes/start-here/quick-start/)
   Register this project in Firstmate with the `no-mistakes` delivery mode.

The gate runs `make lint` and the same type, import, fast test, and regression targets used in CI.
Test remains available for intent-specific evidence.
Review guidance and automatic repair protections come from the accepted default branch.
No-mistakes reruns validation for CI repairs.
GitHub's required checks and code-owner approval enforce merge policy for changes already committed by an implementation agent.
