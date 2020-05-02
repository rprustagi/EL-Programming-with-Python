import sys
import matplotlib.pyplot as plt

# cmd line arguments for y=mx+c
# $1 - m (slope)
# $2 - c (intercept on y axis)
# $3 - number of points (default 6)
if len(sys.argv) < 3:
  print("Usage:", sys.argv[0], "<m> <c> [num of graph pts")
  exit
m = float(sys.argv[1])
c = float(sys.argv[2])
cnt = 6
if len(sys.argv) > 3:
  cnt = int(sys.argv[3])

xval=[i for i in range(cnt)]
yval=[m*i + c for i in range(cnt)]
plt.plot(xval, yval, "bo--",label="y=mx+c")
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Graph for y=" + str(m) + "x+" + str(c))
plt.legend()
plt.show()
