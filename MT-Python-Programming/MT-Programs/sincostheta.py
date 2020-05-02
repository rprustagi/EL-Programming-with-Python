import math
import matplotlib.pyplot as plt

cnt=200
xmax = 4*math.pi
x=[xmax*i/cnt for i in range(cnt)]
y0=[0 for i in range(cnt)]
y1=[math.sin(xmax*i/cnt) for i in range(cnt)]
y2=[math.cos(xmax*i/cnt) for i in range(cnt)]

plt.plot(x,y0,'k--', label="baseline")
plt.plot(x,y1,'b.', label="Sin" +r'$\theta$')
plt.plot(x,y2,'g.', label="Cos" +r'$\theta$')
plt.xlabel(r"$\theta$ values")
plt.ylabel("Sin and cos curves")
plt.xticks([i*math.pi for i in range(5)],
    [r'$0$', r'$\pi$', r'$2\pi$',r'$3\pi$',r'$4\pi$'])
plt.legend()
plt.show()
