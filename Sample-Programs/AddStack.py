# original code taken from
# https://education.pythoninstitute.org/course_datas/display/97/837#
#------------------------
from CStack import *

class AddingStack(Stack):
  def __init__(self):
    Stack.__init__(self)
    self.__sum = 0

  def getSum(self):
    return self.__sum

  def push(self, val):
    self.__sum += val
    Stack.push(self,val)

  def pop(self):
    val = Stack.pop(self)
    self.__sum -= val
    return val

stack = AddingStack()
for i in range(5):
  stack.push(i)
print(stack.getSum())
for i in range(5):
  print(stack.pop())
