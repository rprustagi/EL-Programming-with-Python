import math
import sys
# ans should be close to 3.141592653589793
ans = 1.0
term=0
diff=ans-term
while diff > 10**(-10):
  term = math.sqrt(2+term)
  newans = ans * term / 2
  diff = ans - newans
  ans=newans

print(2/ans)
