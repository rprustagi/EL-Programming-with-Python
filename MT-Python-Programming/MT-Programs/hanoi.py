#!/usr/bin/env python3
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of N discs is transferred from the
left to the right peg.
The value of N is specified by command line argument

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""
from turtle import *
import sys

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/(num_of_disks * 1.0), 1.0, 1-n/(num_of_disks * 1.0))
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        #textinput("Hanoi Tower", "Press any key to continue")
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"s")
    clear()
    try:
        hanoi(num_of_disks, t1, t2, t3)
        write("press q to exit",
              align="center", font=("Courier", 16, "bold"))
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    global t1, t2, t3
    ht(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of num_of_disks discs
    for i in range(num_of_disks,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press s to start game, q to quit",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "s")
    onkey(bye,"q")
    listen()
    return "EVENTLOOP"

if __name__=="__main__":
    global num_of_disks
    num_of_disks = 5
    if (len(sys.argv) > 1):
        num_of_disks = int(sys.argv[1])

    msg = main()
    print(msg)
    mainloop()
