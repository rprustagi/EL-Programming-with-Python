from turtle import *
import sys

def polygon(x,n):
  angle=360/n
  for i in range(n):
    forward(x)
    left(angle)

polygon(1,360)

