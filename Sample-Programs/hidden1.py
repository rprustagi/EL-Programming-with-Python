from Hidden import *

obj = Hidden()
obj.visible()
try:
  obj.__hidden()
except:
  print("failed")

