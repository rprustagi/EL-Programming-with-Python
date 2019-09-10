# hierarchical levels

class Level0:
  Var0 = 100
  def __init__(self):
    self.var0 = 101
  def fun0(self):
    return 102

class Level1(Level0):
  Var1 = 200
  def __init__(self):
    super().__init__()
    self.var1 = 201
  def fun1(self):
    return 202

class Level2(Level1):
  Var2 = 300
  def __init__(self):
    super().__init__()
    self.var2 = 301
  def fun2(self):
     return 302

obj = Level2()
print(obj.Var0, obj.var0, obj.fun0())
print(obj.Var1, obj.var1, obj.fun1())
print(obj.Var2, obj.var2, obj.fun2())


