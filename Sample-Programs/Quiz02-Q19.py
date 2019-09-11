import random
def append(a=[], x=random.randrange(5,6)):
  a.append(x)
  a = a + [x]
  return a

b = append()
c = append()

print(b, c)
print (b is c, b == c)
