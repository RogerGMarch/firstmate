---
name: research-code-quality
description: Design, implement, or review Python research software for readability, modularity, dependency direction, and maintainability. Load for changes to reusable research code, pipeline architecture, or quality rules.
---

# Research code quality

1. Read the callers, existing tests, and the Import Linter contracts in `pyproject.toml`. Trace data, errors, and state through the smallest end-to-end workflow affected by the change.
2. Keep numerical and domain logic in focused functions with explicit inputs and return values. Put filesystem, network, logging, and CLI behavior at the edge. Keep notebooks for exploration and import reusable steps from `src/`.
3. Apply Clean Code and KISS through descriptive domain names, direct control flow, and explicit errors. Apply DRY to shared domain rules when their behavior should change together. Keep incidental similarities separate. Apply YAGNI to speculative frameworks, registries, and extension points.
4. Use a class when it owns state, an invariant, a resource lifetime, or a meaningful interchangeable implementation. Apply SOLID where it fits: single responsibilities, small interfaces at demonstrated boundaries, substitutable implementations, and dependencies that point toward the domain. Prefer composition and ordinary functions for stateless computation.
5. Preserve callers and existing behavior except where the research intent changes them. Test behavior and scientific invariants with small fixtures. Use numerical tolerances supported by the method and exercise malformed or boundary inputs where they matter.
6. Run the project's fast checks and base comparison. Read each tool's finding before refactoring. Keep tests, thresholds, import exemptions, and check coverage intact unless a maintainer explicitly approves the policy change. Explain new inline suppressions and request a decision before weakening validation.

When reviewing, give the file and line, the observable consequence, and the smallest sound correction. Call out speculative restructuring only when removing it materially simplifies the affected workflow. Load `scientific-quality` when the change affects a dataset, experiment, evaluation, or scientific claim.
