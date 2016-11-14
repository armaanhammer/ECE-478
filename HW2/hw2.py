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



#def crossover(parent1_f, parent1_l, parent2_f, parent2_l child1_f, child1_l, child2_f, child2_l);
#   "crossover function"
#   for i in range(len(parent1_l)):
#       child1_f[i] =
#       child1_l[i] =
    #end for loop
#   for i in range(len(parent1_l)):
#       child2_f[i] = #child2 should generally be more random
#       child2_l[i] =
    #end for loop
#   
#   return

#def evaluate ()
#   "determines fitness of genetics"
#   return

#while loop to continue producing lightshows
# 10 steps in sequence
# length can be from 0 - 1 second
#0-4 for freq, 0 being light 1 4 being light 5

def main():
#See http://www.phy.mtu.edu/~suits/notefreqs.html
#F = [261.63, 440, 293.66] #Hz, waves per second, 261.63=C4-note.
F = [0, 1, 2, 3, 4]#, 4, 3, 2, 1, 0, 3] #10 items
L = 5#[5, 5, 5, 5, 5] #.5, .6, .7, .8, .9, 1] #seconds to play sound

    # loop to play a sequence
for i in range(len(F)):

        #LENGTH = L[i]
        #grab frequency based on #
        #if block to convert 0-4 into a specifc freq
        if F[i] == 0:
            FREQUENCY = 25 #261.63
        elif F[i] == 1:
            FREQUENCY = 300 #293.66
        elif F[i] == 2:
            FREQUENCY = 600
        elif F[i] == 3:
            FREQUENCY = 1500
        elif F[i] == 4:
            FREQUENCY = 4000
        
        dlight(FREQUENCY, L)
    #end loop
#evaluate();
#again?

if __name__=="__main__":
    main()
