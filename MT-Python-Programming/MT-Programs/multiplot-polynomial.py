import math
import matplotlib.pyplot as plt

cnt=9
x=[i for i in range(cnt)]
y0=[math.sqrt(i) for i in range(cnt)]
y1=[i for i in range(cnt)]
y2=[i*math.sqrt(i) for i in range(cnt)]
y3=[i*i for i in range(cnt)]
y4=[i*i*i for i in range(cnt)]
y5=[2**i for i in range(cnt)]

#considering 2 rows and 3 columns, 6 grid subareas
fig = plt.figure() # define drawing area object
plt.subplot(231) # subarea 1-left upper corner
plt.plot(x,y0,'k.--', label="sqrt(x)")
plt.legend()

plt.subplot(232) # subarea 2-middle upper grid
plt.plot(x,y1,'bo--', label="linear")
plt.legend()

plt.subplot(233) # subarea 3-right upper corner
plt.plot(x,y2,'r*--', label="x*sqrt(x)")
plt.legend()

plt.subplot(234) # subarea 2-left lower corner
plt.plot(x,y3,'c.--', label="square(x)")
plt.legend()

plt.subplot(235) # subarea 2-middle lower grid
plt.plot(x,y4,'go--', label="cube(x)")
plt.legend()

plt.subplot(236) # subarea 2-right lower corner
plt.plot(x,y5,'y*--', label="exponential(2**x)")
plt.legend()

plt.show()
