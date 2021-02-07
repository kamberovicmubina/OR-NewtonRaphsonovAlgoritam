import numpy as np
import matplotlib.pyplot as plt
from L2_Z1 import *


x = np.arange(-3, 3, 0.01)
y = 3*x*x - 1
plt.figure()
plt.plot(x, y, color='black')
plt.ylim(-3, 3)
x0 = NR(f1, df1, ddf1, 1, 100, 0.00001)
plt.plot(x0, f1(x0), color='red', marker='o')
plt.plot(x0, f1(x0), color='green', marker='x')
x0 = NR(f1, df1, ddf1, 10, 100, 0.00001)
plt.plot(x0, f1(x0), color='green', marker='x')
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('$y=3x*x - 1$')
plt.show()

x = np.arange(-4, 25, 0.01)
y = -(16*x*x -24*x + 5) * np.e**(-x)
plt.figure()
plt.plot(x, y, color='black')
plt.ylim(-10, 4)
x0 = NR(f2, df2, ddf2, 0.5, 100, 0.00001)
x0_1 = NR(f2, df2, ddf2, 2, 100, 0.00001)
x0_2 = NR(f2, df2, ddf2, 10, 100, 0.00001)
plt.plot(x0, f2(x0), color='green', marker='x', markerSize=15)
plt.plot(x0_1, f2(x0_1), color='green', marker='x', markerSize=15)
plt.plot(x0, f2(x0), color='red', marker='o') #ako je x0=0.5
plt.plot(x0_1, f2(x0_1), color='red', marker='o') #ako je x0=2
plt.plot(x0_2, f2(x0_2), color='red', marker='o') #ako je x0=10
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('$y=-(16*x*x -24*x + 5) * e**(-x)$')
plt.show()


x = np.arange(-2, 8, 0.01)
y = np.sin(x) + np.sin((10/3) * x)
plt.figure()
plt.plot(x, y, color='black')
plt.ylim(-2, 2)
x0 = NR(f3, df3, ddf3, 0, 100, 0.000001)
x0_1 = NR(f3, df3, ddf3, 6, 100, 0.000001)
x0_2 = NR(f3, df3, ddf3, 7, 100, 0.000001)
plt.plot(x0, f3(x0), color='green', marker='x', markerSize=15) 
plt.plot(x0_1, f3(x0_1), color='green', marker='x', markerSize=15)
plt.plot(x0_2, f3(x0_2), color='green', marker='x', markerSize=15)
plt.plot(x0, f3(x0), color='red', marker='o') 
plt.plot(x0_1, f3(x0_1), color='red', marker='o')
plt.plot(x0_2, f3(x0_2), color='red', marker='o')
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('$\sin(x) + sin(10*x/3)$')
plt.show()


x = np.arange(-4, 15, 0.01)
y = np.e**(-x)
plt.figure()
plt.plot(x, y, color='black')
plt.ylim(-1, 5)
x0 = NR(f4, df4, ddf4, 1, 3, 0.00001)
x0_1 = NR(f4, df4, ddf4, 10, 100, 0.00001)
plt.plot(x0, f4(x0), color='red', marker='o') 
plt.plot(x0, f4(x0), color='green', marker='x', markerSize=15)
plt.plot(x0_1, f4(x0_1), color='green', marker='x', markerSize=40)
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('$y=e**(-x)$')
plt.show()



































