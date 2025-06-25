import numpy as np
import cv2

img = cv2.imread("my_input.jpg")

cropped = img [50:450, 100:400]

resized = cv2.resize(cropped, (400,200))

cv2.imshow("Original", img)
cv2.imshow("Cropped image", cropped)
cv2.imshow("Resized image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
