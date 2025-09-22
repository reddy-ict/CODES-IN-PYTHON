import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500        # Sampling frequency (Hz)
duration = 1.0  # Duration in seconds
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

f = 5
x = np.sin(2 * np.pi * f * t)

delay = 0.1
x_shifted = np.sin(2 * np.pi * f * (t - delay))

plt.figure(figsize=(10,4))
plt.plot(t, x, label='Original 5 Hz Sine')
plt.plot(t, x_shifted, '--', label='Shifted by 0.1 s')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Time-Shifted 5 Hz Sine Wave')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
