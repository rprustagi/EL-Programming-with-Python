import sys
import math
import matplotlib.pyplot as plt

filename=sys.argv[1]
fh = open(filename)

ldate=[]
lnewcases=[]
lnewdeaths=[]
ltotalcases = []
ltotaldeaths = []
x=[]
xnum = 0

#skip the header line containing column names
fh.readline()

for line in fh:
  line=line.strip()
  date,country,ncases,ndeaths,tcases,tdeaths=line.split(',')
  #print(date,ncases,ndeaths,tcases,tdeaths)
  xnum += 1
  x.append(xnum)
  lnewcases.append(int(ncases))
  lnewdeaths.append(int(ndeaths))
  ltotalcases.append(int(tcases))
  ltotaldeaths.append(int(tdeaths))

#considering 2 rows and 2 columns, 4 grid subareas
fig = plt.figure() # define drawing area object
fig.suptitle("Data starting from March 01, 2020\nx-axis: Number of days from 2020-03-01")
plt.subplot(221) # subarea 1-left upper corner
plt.plot(x,lnewcases,'k.--', label="new cases")
plt.legend()

plt.subplot(222) # subarea 2-right upper corner
plt.plot(x,lnewdeaths,'bo--', label="new deaths")
plt.legend()

plt.subplot(223) # subarea 3-left lower corner
plt.plot(x,ltotalcases,'r*--', label="total cases")
plt.legend()

plt.subplot(224) # subarea 2-right lower corner
plt.plot(x,ltotaldeaths,'c.--', label="total deaths")
plt.legend()

plt.show()
