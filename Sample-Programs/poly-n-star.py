from turtle import *
import sys
sys.argv = ["polystar", 11]
x=100
n=int(sys.argv[1])
outangle = (360/n)
polyangle = 180 - outangle
firstangle = outangle/2
#otherangle = 180 - polyangle/(n-2) # lowermost point
onepartangle = polyangle/(n-2) #highermost point
turnangle = firstangle + outangle + onepartangle
left(firstangle)
for i in range(n):
  forward(x)
  left(turnangle)

input()
