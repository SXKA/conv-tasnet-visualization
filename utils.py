"""Helpers that do not depend on the model stack."""


def trim_to_shortest(*signals):
    """Trim signals to the length of the shortest one along the last axis.

    Works for NumPy arrays and PyTorch tensors of shape (..., time).

    Args:
        *signals: Signals to trim.

    Returns:
        tuple: Trimmed signals, in the same order.
    """

    length = min(signal.shape[-1] for signal in signals)

    return tuple(signal[..., :length] for signal in signals)
