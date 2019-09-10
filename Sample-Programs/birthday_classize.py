# prob: birthday_classsize.py
#-----------------------
""" Problem Description
Let students enter a class one by one.
The entry stops the moment the birthday of new incoming student is same 
as one of those already in the class.
Birthday can be taken as a number between 1 & 365
Conduct 10000 trials and find the average class size when two students have same birthday.

Expected output: 23
INPUT
None

OUTPUT
<Average class size (in int)>
"""
from random import *
#from math import *


trials = 10000
sum = 0
for i in range(trials):
  birthday = [0] * 365
  cnt = 0
  while True:
    num = randrange(0,365)
    if birthday[num] == 1:
      break
    birthday[num] = 1
    cnt += 1
  sum += cnt
print()
print("Average class size for same birthday = ", int(sum/trials))
