#2차원 정규분포의 히스토그램1.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
x=np.random.randn(10000)
mu,sigma=10,2
y=mu+sigma*np.random.randn(10000)

plt.hist2d(x,y,bins=10)
#plt.hist2d(x,y,bins=10,norm=LogNorm())
#plt.hist2d(x,y,bins=10,norm=LogNorm(),cmap=plt.cm.gray)
plt.colorbar()

plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Histogram")
plt.savefig("ex0962.png")
plt.show()
