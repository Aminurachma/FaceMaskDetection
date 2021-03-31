import numpy as np
import cv2

img=cv2.imread("abba.png",0)

def nothing(x):
  pass

cv2.namedWindow('image')

cv2.createTrackbar('min','image',0,255,nothing)
cv2.createTrackbar('max','image',0,255,nothing)

while(1):

 a = cv2.getTrackbarPos('min','image')
 b = cv2.getTrackbarPos('max','image')
 ret,thresh=cv2.threshold(img,a,b,cv2.THRESH_BINARY_INV)
 cv2.imshow("output",thresh)
 k = cv2.waitKey(10) & 0xFF
 if k == 27:
    break

x= cv2.countNonZero(thresh)
cv2.imshow('x',x)
cv2.destroyAllWindows()