import numpy as np

def time_shift(signal, k):
    """Shift the signal by k units."""
    return np.roll(signal, k)

def time_scale(signal, k):
    """Scale the time axis of the signal by factor k."""
    n = len(signal)
    scaled_signal = np.interp(np.linspace(0, n - 1, int(n / k)), np.arange(n), signal)
    return scaled_signal

def signal_addition(signal1, signal2):
    """Add two signals element-wise."""
    if len(signal1) != len(signal2):
        raise ValueError("Signals must have the same length")
    return signal1 + signal2

def signal_multiplication(signal1, signal2):
    """Multiply two signals element-wise."""
    if len(signal1) != len(signal2):
        raise ValueError("Signals must have the same length")
    return signal1 * signal2
