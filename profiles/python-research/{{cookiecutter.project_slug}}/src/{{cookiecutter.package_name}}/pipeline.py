import argparse
import json
import tomllib
from pathlib import Path

from {{ cookiecutter.package_name }}.analysis import sample_mean


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the synthetic example experiment."
    )
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()
    with args.config.open("rb") as stream:
        config = tomllib.load(stream)
    seed = config["seed"]
    sample_size = config["sample_size"]
    if type(seed) is not int or type(sample_size) is not int:
        raise ValueError("seed and sample_size must be integers")
    result = sample_mean(seed=seed, sample_size=sample_size)
    print(json.dumps({"seed": seed, "sample_size": sample_size, "mean": result}))


if __name__ == "__main__":
    main()
