"""Tests for model-independent helpers."""

import numpy as np

from utils import trim_to_shortest


def test_trim_to_shortest_mixed_shapes():
    spk1 = np.ones(100)
    spk2 = np.ones(98)
    mixture = np.ones((1, 101))
    a, b, c = trim_to_shortest(spk1, spk2, mixture)
    assert a.shape == (98,)
    assert b.shape == (98,)
    assert c.shape == (1, 98)


def test_trim_to_shortest_keeps_equal_lengths():
    x = np.arange(5)
    (y,) = trim_to_shortest(x)
    assert np.array_equal(x, y)
