#적분.py
import numpy as np
from scipy.integrate import quad,dblquad,nquad

fx1=lambda x:x**2
a1,e1=quad(fx1,0,10)
print(f'a1={a1}, e1={e1}')

fx2=lambda x,y:x*y**2
a2,e2=dblquad(fx2,0,1,lambda x:0,lambda x:2)
print(f'a2={a2}, e2={e2}')

def bounds_y():return [0,1]
def bounds_x(y):return [0,2]
a3,e3=nquad(fx2,[bounds_x,bounds_y])
print(f'a3={a3}, e3={e3}')
