import numpy as np
import cv2

#Library dari OpenCV = Viola Jones
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

# Sesuaikan nilai ambang dalam rentang 80 hingga 105 berdasarkan cahaya Anda.
bw_threshold = 80

# Masukkan (Variabel yang dibutuhkan)
org = (30, 30)

#Jenis, ukuran, ketebalan, warna Font
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale =  0.45
weared_mask_font_color = (0, 255, 0)
not_weared_mask_font_color = (0, 0, 255)
thickness = 1
weared_mask = "Menggunakan Masker"
not_weared_mask = "Tidak Menggunakan Masker"


# Load Video Webcam
cap = cv2.VideoCapture(0)

while 1:
    # Mendapatkan frame
    ret, img = cap.read()
    img = cv2.flip(img,1)

    # Convert Gambar menjadi Gray Scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert Gambar menjadi hitam dan putih
    (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)
    #cv2.imshow('black_and_white', black_and_white)

    # Mendeteksi Wajah
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Prediksi wajah untuk hitam dan putih
    faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 5)


    if(len(faces) == 0 and len(faces_bw) == 0):
        cv2.putText(img, "Tidak Menemukan Wajah...", org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
    else:
        # Menggambar kotak di area wajah
        for (x, y, w, h) in faces:
            #color = (0, 255, 0)(0, 0, 255) if (len(faces) == 0 and len(faces_bw) == 1) else (0, 0, 255)
            label = "Menggunakan Masker" if (len(faces) == 0 and len(mouth_rects) == 0) else "Tidak Menggunakan Masker"
            cv2.putText(img, label, (x, y- 10), font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            # Deteksi bibir
            mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 5)

        # Wajah terdeteksi tetapi Bibir tidak terdeteksi yang berarti orang tersebut memakai masker
        if(len(mouth_rects) == 0):
            cv2.putText(img, label, (x, y- 10), font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)

            color = (0, 255, 0) if (len(faces) == 0 and len(faces_bw) == 1 and len(mouth_rects) == 0) else (0, 0, 255)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        else:
            for (mx, my, mw, mh) in mouth_rects:

                if(y < my < y + h):
                    # Wajah dan Bibir terdeteksi tetapi koordinat bibir berada dalam koordinat wajah yang 
                    # berarti prediksi bibir benar dan orang tidak memakai masker.
                    cv2.putText(img, label, (x, y- 10), font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)

                    #cv2.rectangle(img, (mx, my), (mx + mh, my + mw), (0, 0, 255), 3)
                    break
            #cv2.rectangle(img, (x, y), (x + w, y + h),(0, 0, 255), 2)
                    

    # Show frame with results
    cv2.imshow('Mask Detection', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release video
cap.release()
cv2.destroyAllWindows()