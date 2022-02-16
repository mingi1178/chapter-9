#test.py
import numpy as np
import cv2
im=cv2.imread("C:/Users/user/Videos/video.png")

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",im)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("ex0990.png",im)
