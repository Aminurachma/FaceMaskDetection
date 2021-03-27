#deteksiwajah.py digunakan untuk mendeteksi wajah berupa foto

import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscale', gray)

# Detect faces in the image
# detectMultiScale = merupakan fungsi umum yang mendeteksi objek. Karena kita memanggilnya pada cascade wajah, itulah yang akan ia deteksi. 
# Opsi pertama adalah sebuah variabel citra dalam mode grayscale.
faces = faceCascade.detectMultiScale( 
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print( "Found {0} faces!".format(len(faces)))
  
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Wajah Terdeteksi!", image)
cv2.waitKey(0)