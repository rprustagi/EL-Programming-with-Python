#--------------------------------------------------------------------
import sys
import math

if len(sys.argv) < 2:
  print("Usage: ", sys.argv[0], "<n1> <n2> <n3>")
  exit(1)
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
n3 = int(sys.argv[3])

if n1 > n2:
  if n1 > n3:
    max=n1
  else:
    max=n3
else:
  if n2 > n3:
    max=n2
  else: 
    max=n3
print("max of %d, %d, and %d is %d" % (n1, n2, n3, max))
#------------------------------------
