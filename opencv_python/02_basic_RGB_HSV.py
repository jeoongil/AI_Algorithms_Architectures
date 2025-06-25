import numpy as np
import cv2

color = cv2.imread("strawberry.jpg", cv2.IMREAD_COLOR)
print(color.shape)

height,width,channels = color.shape
cv2.imshow("Original Image",color)

cv2.waitKey(0)

b,g,r = cv2. split(color)
rgb_split = np.concatenate((b,g,r),axis=1)
cv2.imshow("BGR Channels", rgb_split)

cv2.waitKey(0)

hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

h,s,h = cv2.split(hsv)
hsv_split = np.comcatenate((h,s,v),axis=1)
cv2.imshow("Split HSV", hsv_split)

cv2.waitKey(0)
