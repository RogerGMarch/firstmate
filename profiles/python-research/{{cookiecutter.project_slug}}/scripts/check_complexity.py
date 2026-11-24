"""Reject higher Radon scores on existing functions and complex new functions."""

import os
import subprocess
from collections.abc import Iterable, Iterator
from itertools import chain
from pathlib import Path
from tokenize import detect_encoding
from typing import Any

from radon.visitors import ComplexityVisitor

MAX_NEW_COMPLEXITY = 10


def git(*args: str) -> bytes:
    return subprocess.check_output(("git", *args))


def function_scores(
    blocks: Iterable[Any], parent: tuple[str, ...] = ()
) -> Iterator[tuple[tuple[str, ...], int]]:
    for block in blocks:
        name = (*parent, block.name)
        if hasattr(block, "methods"):
            yield from function_scores(block.methods, name)
            yield from function_scores(block.inner_classes, name)
        else:
            yield name, block.complexity
            yield from function_scores(block.closures, name)


def scores(source: bytes) -> dict[tuple[str, ...], list[int]]:
    encoding, _ = detect_encoding(iter(source.splitlines(keepends=True)).__next__)
    visitor = ComplexityVisitor.from_code(source.decode(encoding))
    result: dict[tuple[str, ...], list[int]] = {}
    for name, score in function_scores(chain(visitor.functions, visitor.classes)):
        result.setdefault(name, []).append(score)
    return result


def main() -> int:
    base_ref = os.environ["BASE_REF"]
    base = git("rev-parse", "--verify", "--end-of-options", base_ref + "^{commit}")
    base_sha = base.decode().strip()
    base_files = git("ls-tree", "-r", "--name-only", "-z", base_sha, "--", "src")
    base_paths = set(base_files.split(b"\0"))
    findings = []
    for path in sorted(Path("src").rglob("*.py")):
        if not path.is_file():
            continue
        current = path.read_bytes()
        previous = (
            git("show", f"{base_sha}:{path.as_posix()}")
            if os.fsencode(path) in base_paths
            else b""
        )
        if current == previous:
            continue
        previous_scores = scores(previous)
        for name, current_values in scores(current).items():
            previous_values = previous_scores.get(name, [])
            for index, score in enumerate(current_values):
                limit = (
                    previous_values[index]
                    if index < len(previous_values)
                    else MAX_NEW_COMPLEXITY
                )
                if score > limit:
                    findings.append(
                        f"{path}: {'.'.join(name)} complexity {score} exceeds {limit}"
                    )
    for finding in findings:
        print(finding)
    return int(bool(findings))


if __name__ == "__main__":
    raise SystemExit(main())
