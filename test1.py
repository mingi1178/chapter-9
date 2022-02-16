#test.py
from PIL import Image
im=Image.open("C:/Users/user/Videos/video.png")
print(im.format,im.size,im.mode)
im.save("ex0983-1.png")
im.show()

im2=Image.new("RGB",(200,200),(0,0,255))
im.paste(im2,(100,100))
im.save("ex0983-2.png")
im.show()
im.close()
