# Combination of pythogoras theorem up to n 
import sys

n=int(sys.argv[1])
if n <5:
  print("No solutions exists for n<5")
  exit()
for c in range(5,n+1):
  for a in range(2,n):
    for b in range(a+1,n):
      if a*a + b*b == c*c:
        print("{2}*{2} = {0}*{0} + {1}*{1} ".format(a, b, c))

