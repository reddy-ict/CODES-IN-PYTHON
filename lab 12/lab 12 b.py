import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500
duration = 2.0
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

f1 = 5   # Frequency of sine wave (Hz)
f2 = 10  # Frequency of cosine wave (Hz)
x1 = np.sin(2 * np.pi * f1 * t)
x2 = np.cos(2 * np.pi * f2 * t)

x_mul = x1 * x2

plt.figure(figsize=(10,4))
plt.plot(t, x_mul, label='Product: 5 Hz sine × 10 Hz cosine')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Element-wise Multiplication of 5 Hz Sine and 10 Hz Cosine')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
