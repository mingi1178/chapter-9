#범례 생성.py
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,num=101)
y1,y2=np.sin(x),np.cos(x)

plt.plot(x,y1,'k--',label="y1=sin(x)")
plt.plot(x,y2,'b-',label="y2=cos(x)")

xmin,xmax,ymin,ymax=x[0],x[-1],-1,1
plt.axis([xmin,xmax,ymin,ymax])

plt.legend(loc="best")
plt.savefig("ex0954.png")
plt.show()
