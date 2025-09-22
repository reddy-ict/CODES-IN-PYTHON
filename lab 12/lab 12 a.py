import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000
duration = 1.0
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

# Generate sine waves
f1 = 5
f2 = 10
x1 = np.sin(2 * np.pi * f1 * t)
x2 = np.sin(2 * np.pi * f2 * t)

x_sum = x1 + x2

plt.figure(figsize=(10,4))
plt.plot(t, x_sum, label='Sum of 5 Hz and 10 Hz Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Combined Sine Wave (5 Hz + 10 Hz)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
