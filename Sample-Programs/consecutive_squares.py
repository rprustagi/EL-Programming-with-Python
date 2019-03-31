from turtle import *

x=100
n=4
angle=360/n
def polygon(x,n):
  for i in range(n):
    forward(x)
    left(angle)
  penup()
  forward(x)
  pendown()

polygon(50,4)
polygon(60,4)
polygon(40,4)

input()
