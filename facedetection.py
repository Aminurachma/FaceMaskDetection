import cv2
import numpy as np
import os
cascPath = "haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
#video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera
video_capture = cv2.VideoCapture(0)
while (True):
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, minSize=(60, 60), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h),(0,255,0), 2)
        cv2.putText(frame, "weared_mask", (x, y- 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2, cv2.LINE_AA)
        # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()