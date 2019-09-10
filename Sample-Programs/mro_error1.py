# MRO Erroneous inheritance
class O:
  pass
class A(O):
  pass
class B(O):
  pass
class X(A,B):
  pass
class Y(B,A):
  pass
class Z(X,Y):
  pass

