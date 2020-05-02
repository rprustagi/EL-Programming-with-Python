import sys

filename = sys.argv[1]
fh = open(filename)
count={}
for line in fh:
  words = line.strip().split()
  for word in words:
    count[word] = count.get(word,0) + 1

wlist = [(v,k) for k,v in count.items()]
print(sorted(wlist, reverse=True)[:5])

