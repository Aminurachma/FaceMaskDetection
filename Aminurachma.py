import numpy as np
import cv2 

#Library dari OpenCV = Viola Jones
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

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

    # Resize Gambar menjadi 340 x 240
    images = cv2.resize(img, (340, 240))
    #cv2.imshow('Resize', resize)

    # Convert Gambar menjadi Gray Scale
    gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Greyscale', gray)

    # Deteksi tepi dengan GaussianBlur dan Canny
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 10, bw_threshold)
    #ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
    #cv2.imshow('Video feed', mask)

    # Convert image ke hitam dan putih
    (thresh, black_and_white) = cv2.threshold(canny, bw_threshold, 255, cv2.THRESH_BINARY)
    #cv2.imshow('black_and_white', black_and_white)

    # Mendeteksi Wajah
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Deteksi Mata
    eye_detect = eye_cascade.detectMultiScale(gray, 1.5, 5)

    # Deteksi mulut
    mouth_detect = mouth_cascade.detectMultiScale(gray, 1.5, 5)
    
    # Deteksi hidung
    nose_detect = nose_cascade.detectMultiScale(gray, 1.5, 5)

    # Mendeteksi wajah untuk hitam dan putih
    faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 5)


    if(len(faces) == 0 and len(faces_bw) == 0):
        cv2.putText(images, "Tidak Menemukan Wajah...", org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
    elif(len(faces) == 0 and len(faces_bw) == 1):
        # It has been observed that for white mask covering mouth, with gray image face prediction is not happening
        cv2.putText(images, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
    else:
        # Menggambar kotak di area wajah
        for (x, y, w, h) in faces:
            #color = (0, 255, 0)(0, 0, 255) if (len(faces) == 0 and len(faces_bw) == 1) else (0, 0, 255)
            #label = "Menggunakan Masker" if (len(faces_bw) ==  1 and len(mouth_rects) == 0) else "Tidak Menggunakan Masker"
            #cv2.putText(img, weared_mask, (x, y- 10), font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
            
            cv2.rectangle(images, (x, y), (x + w, y + h), (0, 255, 0), 2)
            kotak_gray = gray[y:y + h, x:x + w]
            kotak_color = images[y:y + h, x:x + w]

            
            #cv2.imshow('roi',kotak_gray)
            #Didalam kotak dimasukan ke variabel.. jika rec2 x citra asli 
            #dibelakang frame item aja, dibinerkan dikali dengan yang citra asli.. agar nilanya 0 masking

            
            # Membuat masking dengan zeros
            mask = np.zeros((images.shape[:2]), dtype=np.uint8)
            
            #Membuat Rectangle untuk menampilkan wajah
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
            cv2.imshow("Rectangular Mask", mask)

            #Menerapkan masking ke gambar
            masked = cv2.bitwise_and(images, images, mask=mask)
            cv2.imshow("Mask Applied to Image", masked)


            #Konversi RGB ke HSV
            #hsv = cv2.cvtColor(images,cv2.COLOR_BGR2HSV)
            # Parameter HSV
            #lower_b = np.array([0, 10, 62])
            #upper_b = np.array([26, 255, 255])

            # membuat mask HSV hasil dari pengubahan HSV
            #mask_new = cv2.inRange(hsv, lower_b, upper_b)
            #cv2.imshow('Mask', mask_new)

            
            # convert image to binary
            #gray = cv2.cvtColor(roi_gray, cv2.COLOR_BGR2GRAY)
            #_, im_th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
            #th_binary = im_th.copy()
            # Invert floodfilled image
            #th_binary_inv = cv2.bitwise_not(th_binary)
            # Combine the two images to get the foreground.

            #im_out = mask_new | th_binary_inv
            # -----------------------imfill-------------------------
            #contours, hierarchy = cv2.findContours(mask_new, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
            #for contour in contours:
            #    area = cv2.contourArea(contour)
            #    if area > 10:
            #        cv2.drawContours(im_out, [contour], 0, 255, -1)# untuk menambal hole / sebagai imfill
            #    result_new = cv2.bitwise_and(images, images, mask=im_out)
            #cv2.imshow('Masking', result_new)

            # Deteksi mulut
            mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 5)
            
            # Deteksi hidung
            nose_detect = nose_cascade.detectMultiScale(gray, 1.5, 5)

            
        # Wajah terdeteksi tetapi mulut dan hidung tidak terdeteksi yang berarti orang tersebut memakai masker
       
        if(len(mouth_rects) == 0 and len(nose_detect) == 0):
            cv2.putText(images, weared_mask, (x, y- 10), font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
        else:
            for (mx, my, mw, mh) in mouth_rects:

                if(y < my < y + h):
                    # Wajah dan Bibir terdeteksi tetapi koordinat mulut dan hidug berada dalam koordinat wajah yang 
                    # berarti prediksi bibir benar dan orang tidak memakai masker.
                    cv2.putText(images, not_weared_mask, (x, y- 10), font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)

                    #cv2.rectangle(img, (mx, my), (mx + mh, my + mw), (0, 0, 255), 3)
                    break

            cv2.rectangle(images, (x, y), (x + w, y + h),(0, 0, 255), 2)
                    
                    
    #Konversi RGB ke HSV
    #hsv = cv2.cvtColor(images,cv2.COLOR_BGR2HSV)
  #Segmentasi untuk masking
    #mask1= cv2.inRange()
    #mask = cv2.inRange(hsv,mouth_detect,nose_detect)
    #result=cv2.bitwise_and(images,images, mask=mask)
    #cv2.imshow('mask', mask)
    #cv2.imshow('segmentasi', result)
    # load the image, convert it to grayscale

    # Parameter HSV
    #lower_b = np.array([0, 10, 62])
    #upper_b = np.array([26, 255, 255])

    # membuat mask HSV hasil dari pengubahan HSV
    #mask_new = cv2.inRange(hsv, lower_b, upper_b)
    #cv2.imshow('Mask', mask_new)

      
    # Show frame with results
    cv2.imshow('Aminurachma: Mask Detection', images)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release video
cap.release()
cv2.destroyAllWindows()