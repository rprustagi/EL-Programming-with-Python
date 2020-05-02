#--------------------------------------------------------------------
import sys
import math

if len(sys.argv) < 2:
  print("Usage: ", sys.argv[0], "<N>")
  exit(1)
N = int(sys.argv[1])
cnt_prime = 0

#------------------------------------
def chk_prime(num):
  isprime = True
  sqrtnum = int(math.sqrt(num))
  for i in range(2, sqrtnum + 1):
    if num % i == 0:
      isprime = False
      break
  return isprime

#------------------------------------
#check for circular prime number
def circular_prime(num):
  # find length
  len = 0
  temp = num
  while temp > 0:
    len += 1
    temp = temp // 10
  cprime = chk_prime(num) # check primality of given number 
  if cprime is False:
    return cprime
  # check primality for each circular variation number
  next_val = num
  for i in range(1, len):
    next_val = (next_val % 10) * 10**(len - 1) + next_val // 10
    if chk_prime(next_val) is False:
      cprime = False
      break
  return cprime
#------------------------------------
if circular_prime(N):
  print(N, "is circular prime number")
else:
  print(N, "is not circular prime")

# end of program
#------------------------
