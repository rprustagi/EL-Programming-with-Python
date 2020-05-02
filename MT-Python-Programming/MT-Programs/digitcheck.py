#--------------------------------------------------------------------
import sys

# check if digit d occurs in number n
def check(n,d):
  if n == 0:
    return False
  elif n%10 == d:
    return True
  else:
    return check(n//10, d)

if len(sys.argv) != 3:
  print("Usage:", sys.argv[0], "<number>  <digit>")
  exit()
number = int(sys.argv[1])
digit = int(sys.argv[2])
if check(number, digit):
  print("Digit", digit, "exists in number", number)
else:
  print("Digit", digit, "doesn't exist in number", number)
#------------------------------------
