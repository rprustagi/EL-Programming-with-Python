# generate random walk
import sys
import random

# validation checks
if (len(sys.argv) != 2):
  print("Usage: ", sys.argv[0], "<number>")
  exit()


#-------------------
def printgrid():
  for row in grid:
    print(row)
#-------------------
n = int(sys.argv[1])
# generate a grid of n by n
grid = [[0 for i in range(2*n+1)]for i in range(2*n+1)]
row=n
col = n
grid[row][col] = 1
printgrid()
cnt = 0 # number of total moves
while row !=0 and row != 2*n and col != 0 and col !=2*n:
#for i in range(5):
  move = random.randrange(1,5)
  cnt += 1
  grid[row][col]=0
  # 1 = move right
  # 2 = move up
  # 3 = move left
  # 4 = move down
  if move == 1:
    row += 1
  elif move == 2:
    col += 1
  elif move == 3:
    row -= 1
  else:
    col -= 1
  print("move = ({0},{1})".format(row,col))
  grid[row][col]=1
  #printgrid()
print("Total number of moves =", cnt)

