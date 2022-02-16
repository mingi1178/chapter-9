# X, Y 축의 범위 설정.py
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(start=-1,stop=1,num=51)
y=x**2
plt.plot(x,y,'b-',x,y,'r*')
plt.axis([-1,1,0,1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("plot example 3")
plt.savefig("ex0952.png")
plt.show()
