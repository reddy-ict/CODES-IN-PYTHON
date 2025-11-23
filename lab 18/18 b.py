import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import correlate

files = ["C:\Users\reddy\Downloads\download (1).wav","C:\Users\reddy\Downloads\WhatsApp Audio 2025-11-23 at 18.53.40_f90c32f1.mp3","C:/Users/devah/Downloads/periodic_audio.wav"]
audios = [sf.read(f)[0] for f in files]
for i in range(len(audios)):
if audios[i].ndim > 1:
audios[i] = audios[i][:, 0]

autocorr = [correlate(a, a, mode='full') for a in audios]

cross_corr_clean_noisy = correlate(audios[0], audios[1], mode='full')
cross_corr_clean_periodic = correlate(audios[0], audios[2], mode='full')

plt.figure(figsize=(12, 8))

for i, ac in enumerate(autocorr):
plt.subplot(4, 1, i + 1)
plt.plot(ac)
plt.title(f'Autocorrelation: {files[i]}')

plt.subplot(4, 1, 4)
plt.plot(cross_corr_clean_noisy, label='Clean vs Noisy')
plt.plot(cross_corr_clean_periodic, label='Clean vs Periodic')
plt.title('Cross-Correlation')
plt.legend()

plt.tight_layout()
plt.show()

