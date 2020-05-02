#--------------------------------------------------------------------
import sys
#sys.argv = ["a.py", "20,80,30,60,10,25,35,31,41"]
# specify sorted list as comma separaed value without any SPACE
# specify key to search as next argumen
def findmax(list, low, high): #index high is excluded
  if low +1 == high:
    return list[low]
  submax = findmax(list, low, high-1)
  if submax > list[high-1]:
    return submax
  else:
    return list[high-1]


if len(sys.argv) != 2:
  print("Usage:", sys.argv[0], "<a,b,c,...>", "<key>")
  exit()

items = list(map(int,sys.argv[1].split(",")))

max = findmax(items, 0, len(items))
print("max of the list is", max)

#------------------------------------
