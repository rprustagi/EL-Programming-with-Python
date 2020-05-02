#computing e till first n terms.
#--------------------------------
import sys

# sys.argv = ["compute", 5] #uncomment for Idle3.
n = int(sys.argv[1])
x = float(sys.argv[2])
sum = 1.0
term = 1.0

for i in range(1,n+1):
    term = term*x/i
    sum = sum + term
print("Value of e for first", n, "terms =", sum)

#using epsilon method
sum = 1.0
term = 1.0
n=0
while True:
  n += 1
  term = term*x/n
  if term > sys.float_info.epsilon:
    sum += term
  else:
    print("Value of e after", n, "terms is ", sum)
    break
exit()

