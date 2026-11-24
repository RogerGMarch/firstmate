import pytest

from {{ cookiecutter.package_name }}.analysis import sample_mean


def test_simulation_estimates_population_mean() -> None:
    assert sample_mean(seed=42, sample_size=100_000) == pytest.approx(0.5, abs=0.005)
