#사각형 그리기.py
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig=plt.figure()
fig.suptitle("Graphics1",color='b',fontsize=20)

ax=fig.add_subplot(111,aspect='equal')
ax.set_title('Rectangle',color='g',fontsize=14)

ax.add_patch(Rectangle((0.1,0.1),0.2,0.2,facecolor='blue',edgecolor='black'))
ax.add_patch(Rectangle((0.4,0.1),0.2,0.2,linewidth=None,alpha=0.5))
ax.add_patch(Rectangle((0.7,0.1),0.2,0.2,linestyle='solid',fill=False,linewidth=2))

ax.add_patch(Rectangle((0.1,0.4),0.2,0.2,fill=False,linestyle='dashed',linewidth=2))
ax.add_patch(Rectangle((0.4,0.4),0.2,0.2,fill=False,linestyle='dashdot',linewidth=2))
ax.add_patch(Rectangle((0.7,0.4),0.2,0.2,fill=False,linestyle='dotted',linewidth=2))

ax.add_patch(Rectangle((0.1,0.7),0.2,0.2,fill=False,hatch='/'))
ax.add_patch(Rectangle((0.4,0.7),0.2,0.2,fill=False,hatch='\\'))
ax.add_patch(Rectangle((0.7,0.7),0.2,0.2,fill=False,hatch='O'))
plt.savefig("ex0969.png")
plt.show()
