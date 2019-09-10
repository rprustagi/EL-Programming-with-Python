#
class Vhcl:
  pass

class LandVhcl(Vhcl):
  pass

class TrackedVhcl(LandVhcl):
  pass

for v1 in [Vhcl, LandVhcl, TrackedVhcl]:
  for v2 in [Vhcl, LandVhcl, TrackedVhcl]:
    print(issubclass(v1,v2),end='\t')
  print()

