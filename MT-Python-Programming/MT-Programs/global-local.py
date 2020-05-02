#--------------------------------------------------------------------
import sys
import random

def init():
  global cnt
  global xy
  global s

  cnt = 1000000000001
  s = "ab"
  xy=[1,2]


def f_play():
  #global cnt
  global s

  xy.append(3)
  s = "xyz"
  #cnt += 1

#------------------------------------
init()
f_play()
print(xy, s, cnt)
