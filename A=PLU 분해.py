#A=PLU 분해.py
import numpy as np
from scipy import linalg

def forward_sub(L,b):
    n=len(b)
    y=np.zeros(n)
    y[0]=b[0]
    for k in range(1,n):y[k]=(b[k]-np.dot(L[k,0:k],y[0:k]))/L[k,k]
    return y

def backward_sub(U,y):
    n=len(y)
    x=np.zeros(n)
    for k in range(n-1,-1,-1):x[k]=(y[k]-np.dot(U[k,k+1:n],x[k+1:n]))/U[k,k]
    return x

A=np.array([[1.,4.,1.],[1.,6.,-1.],[2.,-1.,2.]])
b=np.array([7,13,5])

P,L,U=linalg.lu(A)
print("P =",P)
print("L =",L)
print("U =",U)

b1=np.dot(P.T,b)
y=forward_sub(L,b1)
x=backward_sub(U,y)
print("x=",x)

y=linalg.solve_triangular(L,b1,lower=True)
x2=linalg.solve_triangular(U,y)
print("x2=",x2)
