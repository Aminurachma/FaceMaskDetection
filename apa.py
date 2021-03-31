Python
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('orange.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]


cv2.imshow('image',img)
cv2.imwrite('segmentasi jeruk.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('orange.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
 
 
cv2.imshow('image',img)
cv2.imwrite('segmentasi jeruk.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()