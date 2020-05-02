import sys

filename = sys.argv[1]
fh = open(filename)
count={}
for line in fh:
  words = line.strip().split()
  for word in words:
    count[word] = count.get(word,0) + 1

wlist = []
for k,v in count.items():
  wlist.append((v,k))
slist = sorted(wlist, reverse=True)
print(slist[:5])
