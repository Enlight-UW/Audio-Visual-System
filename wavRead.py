import wave, struct

song = wave.open('stalker.wav','r')

channels = song.getnchannels()      #stero or mono
sampleWidth = song.getsampwidth()   #bytes per sample?
frameRate = song.getframerate()     #frame rate
frameCount = song.getnframes()      #total frames in song
parameters = song.getparams()       #all parameters as a touple

print("Frame Count : " + str(frameCount))
print("Frame Rate : " + str(frameRate))
print("Sample Width : " + str(sampleWidth))

#jump 1 second into the song
song.setpos(50*frameRate)
#read 1 frames
frame = song.readframes(1)
#unpacked = struct.unpack("l", frame)
#print(frame)
#print(unpacked[0])

#frame = song.readframes(1)
#unpacked = struct.unpack("l", frame)
#print(frame)
#print(unpacked[0])


lastZeroLocation = 0
frequencies = {
    0 : 0
}
a = 0           #most recent sample 
b = 0           #previous sample
c = 0           #2nd previous sample
freq = 0

for x in range(0, int(frameCount/frameRate)):
    for y in range(0, frameRate):                   #read in 1 second interval
        
        sample = song.readframes(1)                 #read 1 sample of the song
        unpacked = struct.unpack("l", frame)        #unpack into a 16 bit integer value
        print(str(sample) + " : " + str(unpacked) + " : " + str(song.tell()))                             #print out the value
        a = y                                       #a = current location
        
        if((a > b) & (c > b)):                       #if the last sample was a zero, essentially
           freq = (b - lastZeroLocation)/frameRate  #get the frequency of the last peak
           lastZeroLocation = b
           print(str(freq))

        c = b
        b = a
           

song.close()

