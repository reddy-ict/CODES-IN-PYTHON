import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500        # Sampling frequency (Hz)
duration = 1.0  # Duration in seconds
t = np.linspace(0, duration, int(fs*duration), endpoint=False)
f = 10  # Hz
x = np.sin(2 * np.pi * f * t)

x_scaled = 3 * x

plt.figure(figsize=(10,4))
plt.plot(t, x, label='Original 10 Hz Sine')
plt.plot(t, x_scaled, '--', label='Scaled (×3)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.t
