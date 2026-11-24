import pytest

from {{ cookiecutter.package_name }}.analysis import sample_mean


def test_sample_mean_is_reproducible() -> None:
    assert sample_mean(seed=42, sample_size=1) == pytest.approx(0.6394267984578837)


def test_sample_mean_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="positive"):
        sample_mean(seed=42, sample_size=0)
