import math
import time
import pyaudio

#sudo apt-get install python-pyaudio
PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.

#Global Chromosomes. all have 10 Alleles
    P1 = [0,1,2,3,4,5,4,3,2,1] #Parent 1
    P2 = [0,1,2,3,4,5,5,5,5,5] #Parent 2
    C1 = [0,0,0,0,0,0,0,0,0,0] #Child 1
    C2 = [0,0,0,0,0,0,0,0,0,0] #Child 2
    
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
#F = [0, 1, 2, 3, 4]#, 4, 3, 2, 1, 0, 3] #10 items
#L = 5#[5, 5, 5, 5, 5] #.5, .6, .7, .8, .9, 1] #seconds to play sound

def crossover(parent1, parent2, child1, child2):
    #since we need to change the globals
    global P1
    global P2
    global C1
    global C2
    #   "crossover function"
    index1 = random.randint(1, len(parent1_l) - 2)
    index2 = random.randint(1, len(parent2_l) - 2):
    parent1 = [3, 2, 5, 1, 0]
    parent2 = [4, 3, 2, 1, 0]
    for i in range(len(parent1_l)):
        child1[i] = parent1[:index1] + parent2[index1:]
        child2[i] = parent1[:index2] + parent2[index2:]
                    
    #end for loop
    return (child1, child2)

#def evaluate ()
#   "determines fitness of genetics"
#   ask user "first or second?"
#   get user response
#   P1 = P2
#   if ( user liked C1
        P2 = C1
    elif
        P2 = C2
        
#   return



def play(F):
# 10 steps in sequence
# length can be from 0 - 1 second
#0-5 for freq, 0 being light 1 4 being light 5. 5 is off
for i in range(len(F)):
        #if block to convert 0-5 into a specifc freq
        wait = 1;
        if F[i] == 0: #Light 1
            FREQUENCY = 25 #261.63
        elif F[i] == 1: #Light 2
            FREQUENCY = 300 #293.66
        elif F[i] == 2:#Light 3
            FREQUENCY = 600
        elif F[i] == 3:#Light 4
            FREQUENCY = 1500
        elif F[i] == 4:#Light 5
            FREQUENCY = 4000
        elif F[i] == 5:#Lights Off
            wait = 0
            
        if(wait)
            dlight(FREQUENCY, L)
        elif(!wait)
            time.sleep(L)
#end of loop
return

def main():
    #Seed Parents?
    #first children
    C1 = P1
    C2 = P2
  #DO
    play(C1)
    play(C2)
    #evaluate
    crossover()
    #again 
  #while(yes)
            
if __name__=="__main__":
    main()
