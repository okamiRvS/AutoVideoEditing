import librosa
import librosa.display
import numpy as np

filename = "media\song\editSong.wav"
 
# Load the audio as a waveform `y`
# Store the sampling rate as `sr`
y, sr = librosa.load(filename)

onset_env = librosa.onset.onset_strength(y, sr=sr,
                                         aggregate=np.median)

# 3. Run the default beat tracker
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,
                                       sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

import matplotlib.pyplot as plt
hop_length = 512
fig, ax = plt.subplots(nrows=2, sharex=True)
times = librosa.times_like(onset_env, sr=sr, hop_length=hop_length)
M = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=hop_length)
librosa.display.specshow(librosa.power_to_db(M, ref=np.max),
                         y_axis='mel', x_axis='time', hop_length=hop_length,
                         ax=ax[0])
ax[0].label_outer()
ax[0].set(title='Mel spectrogram')
ax[1].plot(times, librosa.util.normalize(onset_env),
         label='Onset strength')
ax[1].vlines(times[beats], 0, 1, alpha=0.5, color='r',
           linestyle='--', label='Beats')
ax[1].legend()
plt.show()