# Understand classes in python
class Stack:
  def __init__(self):
    self.__stk = []

  def push(self, val):
    self.__stk.append(val)

  def pop(self):
    val = self.__stk[-1]
    del(self.__stk[-1])
    return val
