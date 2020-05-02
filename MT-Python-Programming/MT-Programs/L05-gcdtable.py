# All relatively prime numbers up to n
import sys

def gcd(a, b):
  while a%b !=0:
    a,b=b, a%b
  return b

n=int(sys.argv[1])
n += 1
for i in range(0,n):
  print(i, sep="", end="")
print()
# first row is all spaces because i=1
print(str(1)+' '*(n-1))

for i in range(2,n):
  print(str(i) + ' ', end="") # for j=1, 1st col is SPACE
  for j in range(2,n):
    if gcd(i,j) == 1:
      print('*', end="")
    else:
      print(' ', end="")
  print()
