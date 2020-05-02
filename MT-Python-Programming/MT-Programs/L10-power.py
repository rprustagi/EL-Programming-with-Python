#--------------------------------------------------------------------
import sys
# i/p: argv[1]: N; argv[2] = K


def power(n, k):
  if k==1:
    return n
  else:
    if k % 2 == 0: #even power
      x = power(n, k//2)
      return x*x
    else: # odd power
      x = power(n, (k-1)//2)
      return n*x*x

if len(sys.argv) != 3:
  print("Usage:", sys.argv[0], "<N> <K>")
  exit()

N = int(sys.argv[1])
K = int(sys.argv[2])
if K<1:
  print("Value of K must be >= 1")
  exit()

print("power(%d,%d)=%d" % (N,K, power(N,K)))
#------------------------------------------------
