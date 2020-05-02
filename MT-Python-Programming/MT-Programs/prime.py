#--------------------------------------------------------------------
import sys
import math

if len(sys.argv) < 2:
  print("Usage: ", sys.argv[0], "<N>")
  exit(1)
N = int(sys.argv[1])

def chk_prime(num):
  isprime = True
  sqrtnum = int(math.sqrt(num))
  for i in range(2, sqrtnum + 1):
    if num % i == 0:
      isprime = False
      break
  return isprime

print(chk_prime(N))
# end of program
#------------------------
