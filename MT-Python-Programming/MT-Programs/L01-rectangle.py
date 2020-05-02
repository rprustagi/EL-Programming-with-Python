from turtle import *
import sys

def rectangle(x,y):
  angle=90
  for i in range(2):
    forward(x); left(angle)
    forward(y); left(angle)

rectangle(100,50)
input()
