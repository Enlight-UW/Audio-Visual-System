import wave, struct

song = wave.open('stalker.wav','r')

channels = song.getnchannels()      #stero or mono
sampleWidth = song.getsampwidth()   #bytes per sample?
frameRate = song.getframerate()     #frame rate
frameCount = song.getnframes()      #total frames in song
parameters = song.getparams()       #all parameters as a touple

#jump 1 second into the song
song.setpos(frameRate)
#read 100 frames
frame = song.readframes(100)
print(frame)

song.close()
