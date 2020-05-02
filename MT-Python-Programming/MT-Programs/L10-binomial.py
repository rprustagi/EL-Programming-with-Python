#--------------------------------------------------------------------
import sys
# i/p: argv[1]: N; argv[2] = K


def binomial(n, k):
  if n==k or k==0:
    return 1
  else:
    return binomial(n-1, k) + binomial(n-1, k-1)

if len(sys.argv) != 3:
  print("Usage:", sys.argv[0], "<N> <K>")
  exit()

N = int(sys.argv[1])
K = int(sys.argv[2])

print("Binomial(%d,%d)=%d" % (N,K, binomial(N,K)))
#------------------------------------------------
