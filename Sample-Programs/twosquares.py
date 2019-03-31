from turtle import *

x=100
n=4
angle=360/n
for i in range(n):
  forward(x)
  left(angle)

penup()
forward(x)
pendown()

for i in range(n):
  forward(x)
  left(angle)

input()
