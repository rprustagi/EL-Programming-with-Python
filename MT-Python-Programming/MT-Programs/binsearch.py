#--------------------------------------------------------------------
import sys
#sys.argv = ["a", "20,80,30,60,10,25,35,31,41", "81"]
# specify sorted list as comma separaed value without any SPACE
# specify key to search as next argumen
def binsearch(key, list, low, high):
  if low  >= high:
    return -1
  mid = (low + high) // 2
  if list[mid] == key:
    return mid
  elif list[mid] > key:
    return binsearch(key, list, low, mid)
  else:
    return binsearch(key, list, mid+1, high)

if len(sys.argv) != 3:
  print("Usage:", sys.argv[0], "<a,b,c,...>", "<key>")
  exit()

items = sys.argv[1].split(",")
key = sys.argv[2]
items.sort()
print("Searching", key, "is List ", items)
idx = binsearch(key, items, 0, len(items))
if idx == -1:
  print("Key", key, "does not exist")
else:
  print("key", key, "is at index", idx)

#------------------------------------
