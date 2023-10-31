import cv2
import time
import os


img=cv2.imread("solar-system.jpg")

cv2.imshow("displayimage",img)
cv2.putText(img,"sun",(20,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
cv2.waitKey(0)