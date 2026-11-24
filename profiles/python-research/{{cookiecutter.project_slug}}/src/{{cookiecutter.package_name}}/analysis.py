from random import Random
from statistics import fmean


def sample_mean(*, seed: int, sample_size: int) -> float:
    """Estimate the mean of a synthetic uniform distribution."""
    if sample_size < 1:
        raise ValueError("sample_size must be positive")
    random = Random(seed)
    return fmean(random.random() for _ in range(sample_size))
