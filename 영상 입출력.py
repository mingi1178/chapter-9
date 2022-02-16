#영상 입출력.py
import matplotlib.pyplot as plt
import matplotlib.image as img
image=img.imread("C:/Users/user/Videos/video.png")
print("image.shape =",image.shape)

plt.imshow(image)
img.imsave("ex0971-1.png",image)
plt.savefig("ex0971-2.png")
plt.show()
