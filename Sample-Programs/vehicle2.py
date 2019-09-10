#
class Vhcl:
  pass

class LandVhcl(Vhcl):
  pass

class TrackedVhcl(LandVhcl):
  pass

vh = Vhcl()
lv = LandVhcl()
tv = TrackedVhcl()

for vr in [vh, lv, tv]:
  for cl in [TrackedVhcl, LandVhcl, Vhcl]:
    print(isinstance(vr, cl),end='\t')
  print()
