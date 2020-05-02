#--------------------------------------------------------------------
import sys

def reverse(list, low, high):
  if low + 1 >= high:
    return
  list[low], list[high-1] = list[high-1], list[low]
  return reverse(list, low+1, high-1)


items = [] # empty list
for i in range(1,len(sys.argv)):
  items.append(sys.argv[i])
print("Given List is ", items)

reverse(items, 0, len(items))
print("Reverse list is ", items)
#------------------------------------
