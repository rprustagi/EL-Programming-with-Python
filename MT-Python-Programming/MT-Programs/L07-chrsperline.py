#--------------------------------------------------------------------
import sys
import math

if len(sys.argv) < 2:
  print("Usage: ", sys.argv[0], "<filename>")
  exit(1)
filename = sys.argv[1]
fh = open(filename)
cnt = 1 # start from first line
for line in fh:
  print("Line %d had %d characters" % (cnt, len(line.rstrip())))
  cnt += 1

#------------------------------------
