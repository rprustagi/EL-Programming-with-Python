# generate ramanujan numbers
import sys
import math

# validation checks
if (len(sys.argv) != 2):
  print("Usage: ", sys.argv[0], "<number>")
  exit()

number = int(sys.argv[1])

# main program
print("Ramanujan numbers for", number, "are:")
aa = 1
count = 0
while (aa**3) <= number:
  bb = aa
  while (aa**3 + bb**3) <= number:
    cc = aa + 1
    while (cc**3) <= number:
      #print(aa,bb,cc)
      dd = cc
      while (cc**3 + dd**3) <= number:
        if ((aa**3 + bb**3) == (cc**3 + dd**3)):
          print("Number: {0} = {1}**3 + {2}**3 = {3}**3 + {4}**3".format(
            aa**3 + bb**3, aa, bb, cc, dd))
        count = count + 1
        dd = dd + 1
      cc = cc + 1
    bb = bb + 1
  aa = aa + 1

exit()
