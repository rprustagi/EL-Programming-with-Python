#MRO valid inheritance

class O:
  pass
class A(O):
  pass
class B(O):
  pass
class X(A,B):
  pass
class Y(A, X):
  pass

