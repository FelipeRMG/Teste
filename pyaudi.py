#!/usr/bin/env python
# -*- coding: utf-8 -*-
# utilizado para gravar o audio
import pyaudio
import wave

CHUNK = 1024						#Frames por segundo
FORMAT = pyaudio.paInt16 			#Formato do audio
CHANNELS = 2 						#1 canal: mono - 2 canais: stereo 
RATE = 44100 						#taxa de amostragem em hertz
RECORD_SECONDS = 5 					#tempo de gravação em segudos
WAVE_OUTPUT_FILENAME = "output.wav" #arquivo de saída de audio

#cria a instância do pyaudio
p = pyaudio.PyAudio()
#configura  a stream para gravar o audio 
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

#configura as características do arquivo de audio
# print frames
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()