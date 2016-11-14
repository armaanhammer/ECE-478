import math
import time
import random
import pyaudio

#sudo apt-get install python-pyaudio
PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.

#Global Chromosomes. all have 10 Alleles
P1 = [0,1,2,3,4,5,4,3,2,1] #Parent 1
P2 = [0,1,2,3,4,5,5,5,5,5] #Parent 2
C1 = [0,1,2,3,4,5,4,3,2,1] #Child 1
C2 = [0,1,2,3,4,5,5,5,5,5] #Child 2
L = 1
    
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

def miccheck():
    "loop to find the light frequencies"
    frq = 10;
    for i in range(0,100):
        print ('freq = ', freq)
        dlight(freq, 5)
        freq = freq + 10
    #end for loop
    return

def crossover():
    "make children"
    #since we need to change the globals
    global C1
    global C2
    #   "crossover function"
    index1 = random.randint(1, len(P1) - 2)
    index2 = random.randint(1, len(P2) - 2)
    for i in range(len(P1)):
        C1[i] = P1[:index1] + P2[index1:]
        C2[i] = P1[:index2] + P2[index2:]
                    
    #end for loop
    return

#def evaluate():
#   "select children for crossover"
#   global P1
#   global P2
#   ask user "first or second?"
#   get user response
#   P1 = P2
#   if ( user liked C1
#        P2 = C1
#   elif
#        P2 = C2
        
#   return



def play(F):
    "play sequence"
# 10 steps in sequence
# length can be from 0 - 1 second
#0-5 for freq, 0 being light 1 4 being light 5. 5 is off
    FREQUENCY = 1
    for i in range(len(F)):
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
        if wait == 1:
            dlight(FREQUENCY, L)
        elif wait == 0:
            time.sleep(L)

def main():
    #Seed Parents?
    #first children
    gen = 0
    again = 1
    while(again):
        play(C1)
        play(C2)
        #evaluate
        crossover()
        gen = gen + 1
        print ('generation ', gen)
        again = input(' again? 1 yes 0 no')
    #end while loop

if __name__=="__main__":
    main()
