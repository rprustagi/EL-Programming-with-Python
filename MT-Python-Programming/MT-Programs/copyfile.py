import sys
sfile=sys.argv[1]
dfile=sys.argv[2]
fhs = open(sfile)
fhd = open(dfile, "w")
cnt=0
for line in fhs:
  fhd.write(line)
  cnt += 1
fhs.close(); fhd.close()
print("Copied", cnt, "lines")
