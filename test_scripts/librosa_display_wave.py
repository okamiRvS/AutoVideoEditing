import librosa
import librosa.display
import numpy as np
from matplotlib import pyplot as plt
import pdb

filename = "media\song\editSong.wav"
 
# Load the audio as a waveform `data`
# Store the sampling rate as `sampling_rate`
data, sampling_rate = librosa.load(filename)

plt.figure(figsize=(12, 4))
pdb.set_trace()
librosa.display.waveplot(data**50, sr=sampling_rate)
plt.show()