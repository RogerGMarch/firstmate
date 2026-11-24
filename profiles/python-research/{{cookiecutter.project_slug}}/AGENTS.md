# Research workflow

- Load [research-code-quality](.agents/skills/research-code-quality/SKILL.md) when changing or reviewing Python code, architecture, or validation rules.
- Load [scientific-quality](.agents/skills/scientific-quality/SKILL.md) when changing research data, methods, experiments, or reported results.
- Run `make check` and `make regression` before handing off a change. Use `make test-science` when the change needs full scientific validation and the required inputs are available.
- Surface changes to tests, suppressions, dependency contracts, or gate configuration for maintainer review. Record what was run and any scientific evidence still needed.
