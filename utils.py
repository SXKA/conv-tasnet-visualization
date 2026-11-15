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


def to_mono(signal):
    """Average the channels of a (channels, time) signal into (1, time).

    Works for NumPy arrays and PyTorch tensors.

    Args:
        signal: Signal of shape (channels, time).

    Returns:
        Signal of shape (1, time).
    """

    if signal.shape[0] == 1:
        return signal

    # torch.Tensor.mean takes keepdim, numpy's takes keepdims.
    if hasattr(signal, "dim"):
        return signal.mean(dim=0, keepdim=True)

    return signal.mean(axis=0, keepdims=True)
