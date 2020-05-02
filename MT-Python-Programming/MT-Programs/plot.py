# to draw graph for y=mx+c
import sys
import matplotlib.pyplot as plt
m=float(sys.argv[1])
c=float(sys.argv[2])
cnt=int(sys.argv[3])

xval=[i for i in range(cnt)]
yval=[m*i+c for i in range(cnt)]
plt.plot(xval, yval,"rv:", label="Linear graph")
plt.xlabel("X Values")
plt.ylabel("Y values")
plt.title("Graph for eqn y=mx+c")
plt.legend()
plt.show()

