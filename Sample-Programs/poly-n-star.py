from turtle import *

x=200
n=11
outangle = (360/n)
polyangle = 180 - outangle
firstangle = outangle/2
otherangle = 180 - polyangle/(n-2)

left(firstangle)
for i in range(n):
  forward(x)
  left(otherangle)

input()
