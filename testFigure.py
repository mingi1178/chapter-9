# test.py
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot([1,3,5,7,9])

size=fig.get_size_inches()
dpi=fig.get_dpi()
print("size =",size)
print("dpi =",dpi)
print("pixel size =",size*dpi)

plt.xlabel("x")
plt.ylabel("y")
plt.title("plot example 1")
plt.show()
