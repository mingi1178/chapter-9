#다중 서브플롯.py
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(num=1,figsize=(6,6),dpi=100,facecolor="#f0f0f0")
size=fig.get_size_inches()
dpi=fig.get_dpi()
print("size =",size)
print("dpi =",dpi)
print("pixel size =",size*dpi)

ax1=fig.add_subplot(2,2,1,facecolor='r')
ax1.plot(range(12))

ax2=fig.add_subplot(2,2,2,facecolor='g')
x=np.linspace(start=-1,stop=1,num=51)
y=x**2
ax2.plot(x,y,'b-')

ax3=fig.add_subplot(2,2,3,facecolor='b')
x=np.linspace(0,2*np.pi,num=51)
y=np.sin(x)
ax3.plot(x,y,'r-')

ax4=fig.add_subplot(2,2,4,facecolor='y')
y=np.cos(x)
ax4.plot(x,y,'r-')
plt.savefig("ex0965.png")
plt.show()
