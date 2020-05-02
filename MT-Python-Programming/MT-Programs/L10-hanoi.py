#--------------------------------------------------------------------
import sys
# i/p: argv[1]: number of discs
def move(n, X, Y):
  print("Move disc", n, "from", X, "to", Y)
  return

def hanoi(n, A, B, C):
  if n==1:
    move(n, A, B)
    return
  hanoi(n-1, A, C, B)
  move(n, A, B)
  hanoi(n-1, C, B, A)

if len(sys.argv) != 2:
  print("Usage:", sys.argv[0], "<N>")
number = int(sys.argv[1])

hanoi(number, "A", "B", "C")
#------------------------------------
