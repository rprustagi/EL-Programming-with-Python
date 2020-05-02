import math
import matplotlib.pyplot as plt

cnt=50
xmax = 2*math.pi
x=[xmax*i/cnt for i in range(cnt)]
y0=[0 for i in range(cnt)]
y1=[math.sin(xmax*i/cnt) for i in range(cnt)]

plt.plot(x,y0,'k--', x,y1,'b.')
plt.show()
