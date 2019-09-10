# prob: find_duplicate.py
#-----------------------
""" Problem Description
Given an array of non zero positive numbers 
Elements of array have value less than array size
Find if a duplicate number exists

CONSTRAINTS
Do not create a new array
You can modify the elements of the array
Do not use a dictionary object
Do not check membership existence of element
  e.g. do not use if elem in arr:

INPUT
2 3 5 1 2 3 3 4 1 1 4 5 7 1 8 1 2

OUTPUT
2 3 5 

"""
import sys
#sys.argv=["p.py", 2, 3, 5, 1, 2, 3, 3]
if (len(sys.argv) < 2):
  print("specify input array of integers")
  print(sys.argv[0], "<a b c ...")
  exit(1)
maxval = len(sys.argv) - 1
arr = [0] * (maxval + 1)
for i in range(1, maxval + 1):
  val = int(sys.argv[i])
  if val > maxval or val <= 0:
    print("element Value", val, "is violating constraints")
    exit(1)
  arr[i] = int(sys.argv[i])

# check for duplicates
for i in range(1, maxval+1):
  val = arr[i] % maxval
  arr[val] += maxval 

# print all the elements which are duplicates
for i in range(1, maxval + 1):
  val = arr[i] - maxval
  if val > 0 and val <= maxval:
    print(i, end=" ")
print()
