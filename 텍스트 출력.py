#텍스트 출력.py
import matplotlib.pyplot as plt
fig=plt.figure()
ax=plt.gca()
ax.axis([0,10,0,10])
ax.set_title('TeX equation')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.text(2,8,"$e{^{ix}} = cos(x) + i\/sin(x)$",style='italic',fontsize=20,bbox={'facecolor':'red','alpha':0.5,'pad':10})
ax.text(2,6,r"parabola equation: $y=ax^2+bx+c$",fontsize=15)
ax.text(2,4,r"$\alpha_i > \beta_i$",fontsize=20)
ax.text(2,2,r"$\sum_{i=0}^\infty x_i$",fontsize=20, color='green')
plt.savefig("ex0967.png")
plt.show()
