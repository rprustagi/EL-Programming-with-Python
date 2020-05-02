#--------------------------------------------------------------------
import sys
import math

if len(sys.argv) < 2:
  print("Usage: ", sys.argv[0], "<N>")
  exit(1)
N = int(sys.argv[1])


#------------------------------------
def fact(num):
  ans = 1
  for i in range(2,num+1):
    ans *= i
  return ans

#------------------------------------
#print all binomial coefficients
for i in range(0, N+1):
  print("Comb({0},{1}) = {2}".format(N, i, fact(N)//(fact(i)*fact(N-i))))
