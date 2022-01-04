#!usr/bin/env python  
#coding=utf-8  

# how to install pyaudio answer of (Joljas Kerketta)
# https://stackoverflow.com/questions/54998028/how-do-i-install-pyaudio-on-python-3-7
from threading import Timer, Thread, Condition, currentThread
import queue
import captureVideo as vid
import pyaudio  
import wave 
import time
import pdb
import librosa

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            
            # get control of the thread
            condition_object.acquire()

            # edit queue increasing his value
            self.args[0].put(self.args[0].get() + 1)

            # release the lock
            condition_object.release()

            # call the function
            self.function(*self.args, **self.kwargs)

def ping(que):
    #print("my thread %s" % str(currentThread().ident))
    vid.MyVideo(que).run()

def dummyfn(que, msg="foo"):
    condition_object.acquire()
    counter = que.get(False)
    print(f"{msg} {counter}")
    que.put(counter)
    condition_object.release()


#define stream chunk   
chunk = 1024  

#open a wav format music  
filename = "Ocean of Island.wav"
#f = wave.open(r"/usr/share/sounds/alsa/Rear_Center.wav","rb")  
f = wave.open(rf"{filename}","rb")  

#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

# # data from librosa to get bpm
# # Load the audio as a waveform `y`
# # Store the sampling rate as `sr`
# y, sr = librosa.load(filename)

# # Run the default beat tracker
# print("Get bpm, wait a bit...")
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
# bpm = round(tempo, 2)

# Convert the frame indices of beat events into timestamps
bpm = 129.20
bps = bpm/60
delay_in_sec = 1/bps

# create lock object
condition_object = Condition()

# create Queue to share counter variable
que = queue.Queue()

# initialize queue, with the counter to zero, otherwise we'll receive a none object
que.put(0)

# play video
t1 = Thread(target=ping, args=(que,))
t1.start()

# run timer
timer = RepeatTimer(delay_in_sec, dummyfn, args=(que, "Timer",))
timer.start()

#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  

# close timer
t1.cl
timer.cancel()

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  