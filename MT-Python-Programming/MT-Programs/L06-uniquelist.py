#--------------------------------------------------------------------
import sys
import math

if len(sys.argv) < 2:
  print("Usage: ", sys.argv[0], "<n1> <n2> <n3>")
  exit(1)
nums = []
for i in range(1,len(sys.argv)):
  nums.append(int(sys.argv[i]))

listsize = len(nums)
newlist = []
for i in range(listsize):
  if nums[i] not in newlist:
    newlist.append(nums[i])

print(newlist)
#------------------------------------
