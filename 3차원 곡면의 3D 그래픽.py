#3차원 곡면의 3D 그래픽.py
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure(figsize=(8,8))
fig.suptitle("$f(x,y)=x^2+y^2$",color='b',fontsize=20)

x=np.linspace(-5,5,7)
y=np.linspace(-5,5,7)
X,Y=np.meshgrid(x,y)
Z=X**2+Y**2

ax1=fig.add_subplot(221,projection='3d')
surf=ax1.plot_wireframe(X,Y,Z)
ax1.set_title('wireframe')

ax2=fig.add_subplot(222,projection='3d')
surf=ax2.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.RdPu)
fig.colorbar(surf)
ax2.set_title('surface')

ax3=fig.add_subplot(223,projection='3d')
surf=ax3.contour(X,Y,Z)
ax3.set_title('contour')

ax4=fig.add_subplot(224,projection='3d')
surf=ax4.scatter(X,Y,Z)
ax4.set_title('scatter')
plt.savefig("ex0973.png",bbox_inches='tight')
plt.show()
