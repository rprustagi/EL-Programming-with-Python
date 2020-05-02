from turtle import *
import sys
n=int(sys.argv[1]) # number of sides
x=int(sys.argv[2]) # size of each diagonal
outangle = (360/n) # compute the external angle
polyangle = 180 - outangle # compute internal angle
firstangle = outangle/2 # angle for first diagonal
turnangle = firstangle + outangle + firstangle # angle for each subsequent angle
left(firstangle) # draw first angle
for i in range(n): # draw all subsequent angle
  forward(x)
  left(turnangle)

input()
