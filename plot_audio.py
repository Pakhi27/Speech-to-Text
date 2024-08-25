import wave
import matplotlib.pyplot as plt
import numpy as np

obj=wave.open("Television.wav","rb")

sample_freq=obj.getframerate()
n_samples=obj.getnframes()
signal_wave=obj.readframes(-1)

obj.close()

t_audio=n_samples/sample_freq
print(t_audio)

signal_array=np.frombuffer(signal_wave,dtype=np.int16)
times=np.linspace(0,t_audio,num=n_samples)
selected_signal = signal_array[:len(times)]  # Slice up to the length of times

plt.figure(figsize=(15,5))
plt.plot(times,selected_signal)
plt.title("audio_signal")
plt.ylabel("Signal-wave")
plt.xlabel("Time(s)")
plt.xlim(0,t_audio)
plt.show()