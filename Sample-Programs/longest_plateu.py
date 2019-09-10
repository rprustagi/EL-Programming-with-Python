# prob: longest_plateu.py
#-----------------------
""" Problem Description
Given an array of integers
Find the location of plateau i.e.
Longest contiguous sequence of equal values, where
values of elements just before and just after this sequence are smaller.
Output the location index in first line and plateu in 2nd line

CONSTRAINTS
None

INPUT
2 3 5 1 2 3 3 4 1 1 1 4 5 7 1 8 1 2

OUTPUT
8
1 1 1
"""
import sys
#sys.argv=["p.py", 2,3,5,1,2,3,3,4,1,1,1,0,5,5,5,5,5,5,4,7,1,8,1,2]
if (len(sys.argv) < 2):
  print("specify input array of integers")
  print(sys.argv[0], "<a b c ...")
  exit(1)

cnt = len(sys.argv)
arr = [0] * cnt
# initialize input array
for i in range(1,cnt):
  arr[i] = int(sys.argv[i])

last_index = 0
last_len = 0
last_val = arr[0]
curr_index = 1
curr_len = 1
curr_val = arr[1]

# check for plateu
for i in range(2,cnt):
  val = arr[i]
  if val == curr_val: #plateu continues
    curr_len += 1
  elif val > curr_val: # not a plateu
    curr_index = i
    curr_len = 1
    curr_val = val
  else: # plateu over
    if last_len < curr_len:
      last_len = curr_len
      last_index = curr_index
      last_val = curr_val
    curr_index = i
    curr_len = 1
    curr_val = val
# check if last seq is plateu
if last_len < curr_len:
  last_len = curr_len
  last_index = curr_index
  last_val = curr_val

# print the location and
print(last_index)
print((str(last_val) + " ") * last_len)
