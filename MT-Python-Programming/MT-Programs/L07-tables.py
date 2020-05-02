#--------------------------------------------------------------------
import sys
import math

if len(sys.argv) < 2:
  print("Usage: ", sys.argv[0], "<N>")
  exit(1)
N = int(sys.argv[1])
for i in range(1,N+1): # tables from 1 to N
  for j in range(1,11): # multiples from 1 to 10
    print("{0} x {1} = {2}".format(i, j, i*j))
  print()

#------------------------------------
