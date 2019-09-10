# Understand classes in python
from CStack import *

s1 = Stack()
s2 = Stack()
s3 = Stack()
s1.push(1)

s1.push(1)
s2.push(s1.pop() + 1)
s3.push(s2.pop() - 2)
print(s3.pop())

