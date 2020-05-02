import math
import sys
r = int(sys.argv[1])

if r < 1:
  print("Invalid input")
  exit()

def fact(n):
  if n==0 or n==1:
    return 1
  ans=1
  for i in range(1,n+1):
    ans = ans * i
  return(ans)

if r==1:
  print(0)
  exit()

fact_r = fact(r)
term = fact_r
sum = term

for i in range(1,r+1):
  term = term * (-1) // i
  sum = sum + term

print(sum)
