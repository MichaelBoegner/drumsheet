import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

# Load audio file
audio, sample_rate = sf.read('./Tycho - Dive.mp3')
# print(audio[10000:10010], sample_rate)
# print(audio[10000:10010].getfield("float64"))
# Create time axis
# time = np.arange(0, len(audio)) / sample_rate

# Plot audio signal
# plt.plot(audio[10000:50000])
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
# plt.show()

plt.figure(figsize=(15, 5))
plt.specgram(audio[50000:50100], Fs=sample_rate, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, 5000)
plt.colorbar()
plt.show()