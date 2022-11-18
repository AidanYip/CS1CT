import math
import wave

frequencies = {'c': 523.25,
               'd': 587.36,
               'e': 659.25,
               'f': 698.46,
               'g': 783.99,
               'a': 880.00,
               'b': 987.84,}

def generatenote(noteletter, duration):
    # generate signal and save to file
    for i in range(int(duration * sampleRate)):
        value = int(32767.0*math.cos(noteletter*math.pi*i/sampleRate))
        data = value.to_bytes(2, 'little', signed=True)
        wavef.writeframesraw(data)


sampleRate = 44100   # hertz
duration = 0.5       # seconds
frequency = 440.0    # 440 hertz corresponds to note A

# initialize wave file
wavef = wave.open('sound.wav','wb')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2)
wavef.setframerate(sampleRate)

nextnote = input("Enter a new note: ")
while nextnote != "":
    generatenote(frequencies[nextnote], duration)
    nextnote = input("Enter a new note: ")

# close wave file
wavef.writeframes(b'')
wavef.close()
'''
the sequence of notes for the Big Ben Westminster chimes is:
'fagcfgafafgccgaf'
'''
