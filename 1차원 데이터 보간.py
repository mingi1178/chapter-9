#1차원 데이터 보간.py
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def error(x,y1):
    y=a*x**3+b*x**2+c*x+d
    e=np.absolute(y-y1)
    return np.sum(e)

N=10
x=np.linspace(-10,10,N)
a,b,c,d=1/4,3/4,-3/2,-2
y=a*x**3+b*x**2+c*x+d
plt.plot(x,y,'o')

f1=interpolate.interp1d(x,y,kind='linear')
xnew=np.arange(x[0],x[-1],0.1)
ynew=f1(xnew)
plt.plot(xnew,ynew,'r-',label='linear')
e1=error(xnew,ynew)
print("e1 =",e1)

f2=interpolate.interp1d(x,y,kind='nearest')
ynew=f2(xnew)
plt.plot(xnew,ynew,'g-',label='nearest')
e2=error(xnew,ynew)
print("e2 =",e2)

f3=interpolate.interp1d(x,y,kind='quadratic')
ynew=f3(xnew)
plt.plot(xnew,ynew,'b-',label='quadratic')
e3=error(xnew,ynew)
print("e3 =",e3)

f4=interpolate.interp1d(x,y,kind='cubic')
ynew=f4(xnew)
plt.plot(xnew,ynew,'k-',label='cubic')
e4=error(xnew,ynew)
print("e4 =",e4)

plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel("$y=ax^3+bx^2+cx+d$",fontsize=20)
plt.title("1D interpolation")
plt.savefig("ex0975.png",bbox_inches='tight')
plt.show()
