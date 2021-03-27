import cv2
import numpy as np
import matplotlib.pyplot as plt
 
#baca gambar
nemo=cv2.imread('y.JPG')
#convert BGR ke RGB
nemo=cv2.cvtColor(nemo,cv2.COLOR_BGR2RGB)
#convert RGK ke HSV
hsv_nemo=cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
 
#deklarasi batas bawah (orange cerah)
light_orange=(1,190,200)
#deklarasi batas atas (dark orange)
dark_orange =(18, 255, 255)
 
#tresholding
mask=cv2.inRange(hsv_nemo,light_orange,dark_orange)
#impose gambar asli dengan mask
result=cv2.bitwise_and(nemo,nemo, mask=mask)
 
#plotiing
plt.subplot(1,4,1)
plt.imshow(nemo)
plt.subplot(1,4,2)
plt.imshow(hsv_nemo)
plt.subplot(1,4,3)
plt.imshow(mask)
plt.subplot(1,4,4)
plt.imshow(result)
plt.show()