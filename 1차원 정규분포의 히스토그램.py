#1차원 정규분포의 히스토그램.py
import numpy as np
import matplotlib.pyplot as plt
mu,sigma=10,1
x=mu+sigma*np.random.randn(10000)
n,bins,patches=plt.hist(x,50,density=True,color='g',label='hist')

pdf=n*np.diff(bins)
print(np.sum(pdf))
middle_x=bins[:-1]+np.diff(bins)/2
plt.plot(middle_x,pdf,'r-',linewidth=1.5,label='pdf')

cdf=np.cumsum(pdf)
plt.plot(middle_x,cdf,'b--',linewidth=2.5,label='cdf')

xmin,xmax=np.amin(x),np.amax(x)
plt.xlim(xmin,xmax)
plt.xlabel("x")
plt.ylabel("Prob(x)")
plt.title("Histogram of N(10, 1)")
plt.grid(True)
plt.legend(loc="best")
plt.savefig("ex0960.png")
plt.show()
