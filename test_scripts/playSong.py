#!usr/bin/env python  
#coding=utf-8  

# how to install pyaudio answer of (Joljas Kerketta)
# https://stackoverflow.com/questions/54998028/how-do-i-install-pyaudio-on-python-3-7
import pyaudio  
import wave 
import time
import pdb

#define stream chunk   
chunk = 1024  

#open a wav format music  
f = wave.open(r"media/song/Ocean of Island.wav","rb")  

#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True) 

pdb.set_trace()

#read data  
data = f.readframes(chunk)  

#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  