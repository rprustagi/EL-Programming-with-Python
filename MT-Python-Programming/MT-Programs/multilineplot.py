import sys
import matplotlib.pyplot as plt

cnt=4
x=[i for i in range(-cnt,cnt,1)]
y1=[i for i in range(-cnt,cnt,1)]
y2=[i*i for i in range(-cnt,cnt,1)]
y3=[i*i*i for i in range(-cnt,cnt,1)]
plt.plot(x,y1,'b*-', x,y2,'ro--', x,y3,'gs-.')
plt.show()
