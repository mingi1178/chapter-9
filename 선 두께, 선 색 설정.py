#선 두께, 선 색 설정.py
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,num=51)
y=np.sin(x)
line=plt.plot(x,y)
xmin,xmax,ymin,ymax=np.amin(x),np.amax(x),-1,1
plt.axis([xmin,xmax,ymin,ymax])
#plt.xlim(xmin,xmax)
#plt.ylim(ymin,ymax)
plt.plot([xmin,xmax],[0,0],color='black',linewidth=4.0)
plt.setp(line,color='red',linewidth=2.0)
plt.xlabel("x")
plt.ylabel("y")
plt.title("plot example 4")
plt.savefig("ex0953.png")
plt.show()
