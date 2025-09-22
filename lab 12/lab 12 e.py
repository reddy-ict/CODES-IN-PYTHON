import numpy as np
import matplotlib.pyplot as plt

fs = 500        # Sampling frequency (Hz)
duration = 1.0  # Duration in seconds
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

f = 5  # Hz
x = np.sin(2 * np.pi * f * t)
x_rev = x[::-1]

plt.figure(figsize=(10,4))
plt.plot(t, x, label='Original 5 Hz Sine')
plt.plot(t, x_rev, '--', label='Time-Reversed')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Time-Reversed 5 Hz Sine Wave')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
