from __future__ import division
import math
from math import atan2,degrees,pi
import pygame
from pygame.locals import *


pygame.init()
display_width = 1000
display_height = 800

window = pygame.display.set_mode([display_width,display_height])
pygame.display.set_caption("Fuzzy Logic Simulation")
clock = pygame.time.Clock()

white = (255,255,255)
# importing images
robotImg = pygame.image.load("robot.png")
obsImg = pygame.image.load("obstacle.png")

# Define object locations on window
def rob(x,y):
    window.blit(robotImg,(x,y))

def obs(x,y):
    window.blit(obsImg,(x,y))

# Initialize starting position of object and robot 
rx = (display_width * 0.45)
ry = (display_height * 0.8)

ox = (display_width * 0.70)
oy = (display_height * 0.2)


# Calculate distance between two points
def distance(ox,oy,rx,ry):
    return math.hypot(rx - ox, ry - oy)

def angle(ox,oy,rx,ry):
    dx = ox - rx
    dy = oy - ry
    rads = atan2(-dy,dx)
    rads %= 2 * pi
    degs = degrees(rads)
    return degs

# This is our fuzzy logic class and membership functions
class FuzzySet(object):
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def membership(self, x, y):
        temp = int(y)
        if (temp == 100):
            if (x < self.x1 or x > self.x2):
                return 0.0
            elif (x <= 20):
                return 1
            elif (x > 20 and x <= 40):
                return 4/5
            elif (x > 40 and x <= 60):
                return 3/5
            elif (x > 60 and x < 80):
                return 2/5
            elif (x >= 80):
                return 1/5

        if (temp == 180):
            if (x < self.x1 or x > self.x2):
                return 0.0
            if (x > 0 and x <= 60):
                return 0.3
            if (x > 60 and x <= 120):
                return 1.0
            if (x > 120 and x <= 180):
                return 0.7
    
# Settin up the input variables
# Distance are measured in centimeters
VeryClose = FuzzySet(-1000, 20)
Close = FuzzySet(20, 40)
Medium = FuzzySet(40, 60)
Far = FuzzySet(60, 80)
VeryFar = FuzzySet(80,1000)

# Angles are measured in degrees
Right = FuzzySet(0, 60)
Middle = FuzzySet(60, 120)
Left = FuzzySet(120, 180)


def action(Angle,Distance):
    Output_command = ""
    Output = 0.0
    # Fuzzification Rules
    Output += Middle.membership(Angle,180) * VeryFar.membership(Distance,100)
    Output += Middle.membership(Angle,180) * Far.membership(Distance,100)
    Output += Middle.membership(Angle,180) * Medium.membership(Distance,100)
    Output += Middle.membership(Angle,180) * Close.membership(Distance,100)
    Output += Middle.membership(Angle,180) * VeryClose.membership(Distance,100)

    Output += Right.membership(Angle,180) * VeryFar.membership(Distance,100)
    Output += Right.membership(Angle,180) * Far.membership(Distance,100)
    Output += Right.membership(Angle,180) * Medium.membership(Distance,100)
    Output += Right.membership(Angle,180) * Close.membership(Distance,100)
    Output += Right.membership(Angle,180) * VeryClose.membership(Distance,100)

    Output += Left.membership(Angle,180) * VeryFar.membership(Distance,100)
    Output += Left.membership(Angle,180) * Far.membership(Distance,100)
    Output += Left.membership(Angle,180) * Medium.membership(Distance,100)
    Output += Left.membership(Angle,180) * Close.membership(Distance,100)
    Output += Left.membership(Angle,180) * VeryClose.membership(Distance,100)

    # Defuzzification
    if Output != 0:
        if Output == 0.42 or Output == 0.5599999999999999:
            Output_command = "Turn Right"
        elif Output == 0.24 or Output == 0.18:
            Output_command = "Turn Left"
        elif Output == 0.6 or Output == 0.8:
            Output_command = "Slow Down"
        elif Output == 0.3 or Output == 1.0 or Output == 0.7:
            Output_command = "Stop"
        else:
            Output_command = "MoveForward"

    return Output_command

# Determine movement based on fuzzy logic
def movement(robotx,roboty,move_type):
    if move_type == "MoveForward":
        roboty -= 5
    elif move_type == "Slow Down":
        roboty -= 2
    elif move_type == "Turn Right":
        robotx += 5
        roboty += 5
    elif move_type == "Turn Left":
        robotx -= 5
        roboty += 5
    return robotx,roboty

# Event logic loop
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True

    # Get angle, distance and behavior of fuzzy logic

    Angle = angle(ox,oy + 125,rx,ry)
    Distance = distance(ox,oy + 125,rx,ry)

    if Angle in range(0,181):
        Behavior = action(Angle, Distance)
    else:
        Behavior = "MoveForward"


    print "This is the angle and distance between the two objects.------------"
    print "{},  {},     {}".format(Angle,Distance,Behavior)

    rx,ry = movement(rx,ry,Behavior)

    window.fill(white)
    rob(rx,ry)
    obs(ox,oy)

    pygame.display.update()
    clock.tick(5)


pygame.quit()
quit()






























































