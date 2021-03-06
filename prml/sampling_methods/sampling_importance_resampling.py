import numpy as np


def sir(func, dist, n):
    """
    sampling-importance-resampling

    Parameters
    ----------
    func : callable
        (un)normalized distribution to be sampled from
    dist
        distribution to generate sample
    n : int
        number of samples to draw

    Returns
    -------
    sample : (n, ndim) ndarray
        generated sample
    """
    assert hasattr(dist, "draw"), "the distribution has no method to draw random samples"
    sample_candidate = dist.draw(n * 10)
    weight = np.squeeze(func(sample_candidate)) / dist.proba(sample_candidate)
    assert weight.shape == (n * 10,), weight.shape
    weight /= np.sum(weight)
    index = np.random.choice(n * 10, n, p=weight)
    sample = sample_candidate[index]
    return sample
