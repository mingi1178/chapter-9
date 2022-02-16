#다중 Figure.py
import numpy as np
import matplotlib.pyplot as plt
fig1, (ax1, ax2) = plt.subplots(1,2)
print(fig1.number)    # 1
fig1.suptitle("Figure1")
ax1.set_title('Line: y = x')
ax1.set_facecolor("red")
ax1.plot(range(12))

x=np.linspace(start=-1,stop=1,num=51)
y=x**2
ax2.set_title('Parabola: y = x**2')
ax2.set_facecolor("green")
ax2.plot(x,y,'b-')
plt.savefig("ex0966-1.png")

fig2, (ax3, ax4) = plt.subplots(1,2)
print(fig2.number)    # 2
fig2.suptitle("Figure2")
x=np.linspace(0,2*np.pi,num=51)
y=np.sin(x)
ax3.set_title('y = sin(x)')
ax3.set_facecolor("blue")
ax3.plot(x,y,'r-')

y=np.cos(x)
ax4.set_title('y = cos(x)')
ax4.set_facecolor("yellow")
ax4.plot(x,y,'r-')
plt.savefig("ex0966-2.png")
plt.show()
