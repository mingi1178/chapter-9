#균등분포의 히스토그램.py
import numpy as np
import matplotlib.pyplot as plt
x=np.random.randint(1,11,size=1000)
n,bins,patches=plt.hist(x,10,density=True,color='g')
print(np.sum(n*np.diff(bins)))

xmin,xmax=np.amin(x),np.amax(x)
plt.xlim(xmin,xmax)
plt.xlabel("x")
plt.ylabel("Prob(x)")

plt.title("Histogram of U[1, 10]")
plt.savefig("ex0959.png")
plt.show()
