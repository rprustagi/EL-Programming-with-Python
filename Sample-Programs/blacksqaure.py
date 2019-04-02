from turtle import *

def blacksquare(x):
  angle=90
  for i in range(x//2):
    forward(x); left(90)
    forward(1); left(90)
    forward(x); right(90)
    forward(1); right(90)

blacksquare(40)
input()
