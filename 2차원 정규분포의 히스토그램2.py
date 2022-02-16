#2차원 정규분포의 히스토그램2.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
x=np.random.randn(10000)
mu,sigma=10,2
y=mu+sigma*np.random.randn(10000)
H,xedges,yedges=np.histogram2d(x,y,bins=(10,10))

plt.matshow(H,norm=LogNorm())
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Histogram: plt.matshow()")
plt.savefig("ex0963-1.png")
plt.show()

plt.pcolormesh(xedges,yedges,H,norm=LogNorm())
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Histogram: plt.pcolormesh()")
plt.savefig("ex0963-2.png")
plt.show()

plt.imshow(H,norm=LogNorm())
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Histogram: plt.imshow()")
plt.savefig("ex0963-3.png")
plt.show()

plt.imshow(H,norm=LogNorm(),cmap=plt.cm.gray)
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Histogram: plt.imshow()")
plt.savefig("ex0963-4.png")
plt.show()
