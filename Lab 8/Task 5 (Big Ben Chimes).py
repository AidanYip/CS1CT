import math
import simpledate
import wave

frequencies = {'b': 493.92,
               'c': 523.25,
               'e': 659.25,
               'f': 698.46,
               'g': 783.99,
               'a': 880.00}

def generatenote(noteletter, duration):
    # generate signal and save to file
    for i in range(int(duration * sampleRate)):
        value = int(32767.0*math.cos(noteletter*math.pi*i/sampleRate))
        data = value.to_bytes(2, 'little', signed=True)
        wavef.writeframesraw(data)

def rest(duration):
    for i in range(int(duration * sampleRate)):
        value = 0
        data = value.to_bytes(2, 'little', signed=True)
        wavef.writeframesraw(data)
    

sampleRate = 44100   # hertz
duration = 1.0       # seconds
frequency = 440.0    # 440 hertz corresponds to note A

# initialize wave file
wavef = wave.open('bigbenchimes.wav','wb')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2)
wavef.setframerate(sampleRate)

hour = simpledate.currenthour()
if hour > 12:
    hour -= 12
for i in range(hour):
    generatenote(frequencies["b"], duration)
    rest(duration)
    
# close wave file
wavef.writeframes(b'')
wavef.close()
