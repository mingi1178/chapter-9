#산포도.py
import numpy as np
import matplotlib.pyplot as plt
#ax=fig.add_subplot(111)
#ax.add_patch(patches.Rectangle((0.1,0.4),0.2,0.2,fill=False,linestyle='dashed',linewidth=2))
N=100
x=np.random.randn(N)
mu,sigma=10,2
y=mu+sigma*np.random.randn(N)

plt.rc('figure',figsize=(6,6))
fig,ax=plt.subplots(2,2)
fig.suptitle("Scatter diagram")

ax[0][0].plot(x,y,"o")

ax[0][1].scatter(x,y,color='b',s=10,marker='+')

colors=np.random.rand(N)
ax[1][0].scatter(x,y,c=colors,s=10,marker='o',alpha=.4)

size1=np.random.randint(1,101,size=N)
ax[1][1].scatter(x,y,c=colors,s=size1,marker='o',alpha=.4)
plt.savefig("ex0968.png")
plt.show()
