from turtle import *
import sys

def blackbox (side,angle):
     for i in range(side//2):
        forward(side); left(angle) # draw black square
        forward(1); left(angle)
        forward(side); right(angle)
        forward(1); right(angle)
     right(angle) # move to next point where to draw square
     forward(side)
     left(angle)

def whitebox (side, angle): # draw white box
    for i in range(4):
        forward(side)
        left(angle)

def rowwithblack(m,side,angle):
    for i in range(m//2):
        blackbox(side,angle)
        forward(side)
        whitebox(side,angle)
        forward(side)
    forward(-m*side)

def rowwithwhite(m,side,angle):
    for i in range(m//2):
        whitebox(side,angle)
        forward(side)
        blackbox(side,angle)
        forward(side)
    forward(-m*side)

angle=90
def chessboard(m,side):
     for i in range(m//2):
         rowwithblack(m,side,angle)
         left(angle)
         forward(side)
         right(angle)
         rowwithwhite(m,side,angle)
         left(angle)
         forward(side)
         right(angle)


#----------------------------------------------------------------------
#main program
n=8
size=int(sys.argv[1])
chessboard(n,size)
input("")
