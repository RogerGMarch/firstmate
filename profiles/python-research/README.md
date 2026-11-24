# Python research profile

Generate a project from a Firstmate checkout with [uv](https://docs.astral.sh/uv/) and [Cookiecutter](https://cookiecutter.readthedocs.io/).

```sh
uvx --from cookiecutter==2.6.0 cookiecutter profiles/python-research
```

Supply a GitHub user or team with write access as `quality_owner` if the repository will use GitHub merge protection.
For a local template archive, substitute the extracted directory for `profiles/python-research`.
The generated README explains local checks and how to enable the protections on GitHub and in Firstmate.
The initial project includes a locked, synthetic example with fast and separately runnable scientific tests.

To adopt the profile in an existing research project, generate a reference project and copy the two `.agents/skills/` directories.
Add their triggers to the project's existing `AGENTS.md`.
Merge the Make targets, tool settings, and gate settings with the project's own configuration.
Set the Import Linter root and layers to the actual architecture, resolve the project's own lockfile, and keep existing validation rules in place.
Adapt the default-branch references if the project uses a branch other than `main`.

The template follows the [Cookiecutter Data Science layout](https://cookiecutter-data-science.drivendata.org/).
The scientific skill uses [FAIR4RS](https://doi.org/10.15497/RDA00068) and the [REFORMS checklist](https://doi.org/10.1126/sciadv.adk3452).
