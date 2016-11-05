from __future__ import division
import math
from math import atan2,degrees,pi
import pygame
from pygame.locals import *

# Initialize pygame and window size
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

ox = (display_width * 0.48) # for middle range, use 0.43 - 0.47/ Anything outside this will cause it to turn right or left
oy = (display_height * 0.2)


# Calculate distance between two points
def distance(ox,oy,rx,ry):
    return math.hypot(rx - ox, ry - oy)

# Calculate angle between both objects
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
            elif (x <= 50):
                return 1
            elif (x > 50 and x <= 100):
                return 4/5
            elif (x > 100 and x <= 175):
                return 3/5
            elif (x > 175 and x < 300):
                return 2/5
            elif (x >= 300):
                return 1/5
            else:
                return 0.0

        if (temp == 180):
            if (x < self.x1 or x > self.x2):
                return 0.0
            if (x > 0 and x <= 60):
                return 0.3
            if (x > 60 and x <= 120):
                return 1.0
            if (x > 120 and x <= 180):
                return 0.7
            else:
                return 0.0
    
# Settin up the input variables
# Distance are measured in centimeters
VeryClose = FuzzySet(-1000, 50)
Close = FuzzySet(50, 100)
Medium = FuzzySet(100, 175)
Far = FuzzySet(175, 300)
VeryFar = FuzzySet(300,1000)

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

# Determine movement based on fuzzy logic, return new position
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
    else:
        pass
    return robotx,roboty

# Event logic loop
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True

    # Get angle, distance and behavior of fuzzy logic. adding 64 finds the center coordinance of the images instead of using top left coordinances 
    ang = angle(ox + 64,oy + 64,rx + 64,ry)

    # Make sure angle is within 0 - 180 degrees. 
    if (ang >= 0.1 and ang <= 180.0):
        dis = distance(ox + 64,oy + 64,rx + 64,ry)
        Behavior = action(ang, dis)
    else:
        print "the angle is greater or less than 0-------------------------------------"
        Behavior = "MoveForward"

    print "This is the angle and distance between the two objects.------------"
    print "{},  {},     {}".format(ang,dis,Behavior)

    # Get new coordinance for robot
    rx,ry = movement(rx,ry,Behavior)

    window.fill(white)
    rob(rx,ry)
    obs(ox,oy)

    pygame.display.update()
    clock.tick(5)   # This is frames per second

pygame.quit()
quit()






























































