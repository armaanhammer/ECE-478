import math
import pyaudio

#sudo apt-get install python-pyaudio
PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.

def dlight (FREQUENCY, LENGTH):
    "plays a frequency for a length"
    
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''
    
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/(2*math.pi)))*127+128))
    
    #fill remainder of frameset with silence
    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA+chr(128)

    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1),
                    channels = 1,
                    rate = BITRATE,
                    output = True)
                    stream.write(WAVEDATA)
stream.stop_stream()
    stream.close()
    p.terminate()
    return

#See http://www.phy.mtu.edu/~suits/notefreqs.html
#F = [261.63, 440, 293.66] #Hz, waves per second, 261.63=C4-note.
F = [0, 1, 2, 3, 4]#, 4, 3, 2, 1, 0, 3] #10 items
L = [1, 5, 1, 5, 5] #.5, .6, .7, .8, .9, 1] #seconds to play sound

def crossover(parent1_f, parent2_f, child1_f, child2_f);
    #   "crossover function"
    index1 = random.randint(1, len(parent1_l) - 2)
    index2 = random.randint(1, len(parent2_l) - 2):
    parent1_f = [3, 2, 5, 1, 0]
    parent2_f = [4, 3, 2, 1, 0]
        for i in range(len(parent1_l)):
            child1_f[i] = parent1_f[:index1] + parent2_f[index1:]
                child2_f[i] = parent1_f[:index2] + parent2_f[index2:]
                    
                    #end for loop
                    return (child1_f, child2_f)


#def evaluate ()
#   "determines fitness of genetics"
#   return

#while loop to continue producing lightshows
# 10 steps in sequence
# length can be from 0 - 1 second
#0-4 for freq, 0 being light 1 4 being light 5

# loop to play a sequence
for i in range(len(F)):
    #grab frequency based on #
    LENGTH = L[i]
        #grab frequency based on #
        #if block to convert 0-4 into a specifc freq
        if F[i] == 0:
            FREQUENCY = 25 #261.63
    elif F[i] == 1:
        FREQUENCY = 250 #293.66
        elif F[i] == 2:
            FREQUENCY = 600
elif F[i] == 3:
    FREQUENCY = 1500
        elif F[i] == 4:
            FREQUENCY = 4000
        
        dlight(FREQUENCY, LENGTH)
#end loop
#evaluate();
#again?
