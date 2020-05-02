#--------------------------------------------------------------------
import sys

# check if the given number is perfect
def perfect(num):
  sum = 1
  for i in range(2, num):
    if num % i == 0:
      sum += i
  if sum == num:
    return True
  else:
    return False

if len(sys.argv) < 2:
  print("Usage: ", sys.argv[0], "<N> ")
  exit(1)

N = int(sys.argv[1])

for i in range(6, N+1):
  if perfect(i):
    print(i)
#------------------------------------
