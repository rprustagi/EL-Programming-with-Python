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


s = Stack()
s.push(10)
s.push(5)
s.push(1)

for i in range(3):
  print(s.pop())
