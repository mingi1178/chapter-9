#bar() 함수.py
import numpy as np
import matplotlib.pyplot as plt
n=10
x=np.random.randint(1,n+1,size=1000)

hist,bin_edges=np.histogram(x,bins=n)
plt.bar(bin_edges[:-1]+0.5,hist,width=np.diff(bin_edges))
plt.xlim(min(bin_edges),max(bin_edges))

plt.xlabel("x")
plt.ylabel("frequency")
plt.title("Histogram")
plt.grid(True)
plt.savefig("ex0961.png")
plt.show()
