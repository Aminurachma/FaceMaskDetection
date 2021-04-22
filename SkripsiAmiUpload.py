# Import Library
import numpy as np
import cv2 
import PIL
from PIL import Image
import sys

# Library dari OpenCV = Viola Jones
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

# Sesuaikan nilai ambang dalam rentang 80 hingga 105 berdasarkan cahaya Anda.
bw_threshold = 80

# Masukkan (Variabel yang dibutuhkan)
org = (30, 30)

# Jenis, ukuran, ketebalan, warna Font
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale =  0.45
weared_mask_font_color = (0, 255, 0)
not_weared_mask_font_color = (0, 0, 255)
thickness = 1
weared_mask = "Menggunakan Masker"
not_weared_mask = "Tidak Menggunakan Masker"
basewidth = 150

# Mengambil path citra
imagePath = sys.argv[1]
img = cv2.imread(imagePath)

# Menampilkan citra dengan ukuran asli
cv2.imshow('Citra Asli', img)
print("Ukuran Citra = ",img.shape)

# Resize Gambar menjadi 40persen lebih kecil dari aslinya
scale_percent =  40
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
images = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Citra hasil Resize', images)
# cv2.imwrite('hasilresize2.png', images)

# Konversi citra ke citra Gray Scale
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
cv2.imshow('Citra Greyscale', gray)

# Deteksi tepi dengan GaussianBlur dan Canny
blur = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(blur, 10, bw_threshold)
#ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
#cv2.imshow('Video feed', mask)

# Konversi citra ke citra hitam dan putih
(thresh, black_and_white) = cv2.threshold(canny, bw_threshold, 255, cv2.THRESH_BINARY)
#cv2.imshow('black_and_white', black_and_white)

# Mendeteksi Wajah
faces = face_cascade.detectMultiScale(gray, 1.1, 5,cv2.CASCADE_SCALE_IMAGE)

# Deteksi Mata
eye_detect = eye_cascade.detectMultiScale(gray, 1.5, 5)

# Deteksi mulut
mouth_detect = mouth_cascade.detectMultiScale(gray, 1.5, 5)
    
# Deteksi hidung
nose_detect = nose_cascade.detectMultiScale(gray, 1.5, 5)

# Mendeteksi wajah untuk hitam dan putih
faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 5)

# Untuk mendeteksi wajah
if(len(faces) == 0 and len(faces_bw) == 0):
    cv2.putText(images, "Tidak Menemukan Wajah...", (95,172), font, 0.4, (255,255,255), thickness, cv2.LINE_AA)

# Untuk mendeteksi wajah yang menggunakan masker putih 
elif(len(faces) == 0 and len(faces_bw) == 1):
    cv2.putText(images, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
else:
    # Menggambar kotak di area wajah untuk melihat wajah yang terdeteksi
    for (x, y, w, h) in faces:     
        cv2.rectangle(images, (x, y), (x + w, y + h), (255, 255, 255), 2)

        # Hasil piksel dari kotak didalam wajah dalam citra greyscale
        kotak_gray = gray[y:y + h, x:x + w]
        #kotak_color = images[y:y + h, x:x + w]
        
        # Menampilkan citra yang terdeteksi sebagai wajah
        cv2.imshow('Citra deteksi Wajah', images)
        
        # Menampilkan potongan masing2 wajah dalam kotak
        cv2.imshow(str(w) + str(h) + '_faces', kotak_gray)

        # Menghitung jumlah wajah yang terdeteksi
        wajah = (len(faces))
        
        # Membuat masking dengan zeros
        mask = np.zeros((images.shape[:2]), dtype=np.uint8)

        # Membuat Rectangle untuk menampilkan wajah
        #cv2.imshow(str(w) + str(h) + '_faces', kotak_gray)

    print("Jumlah wajah ada",wajah)
           
        
    for (x, y, w, h) in faces: 
        # Membuat Rectangle untuk menampilkan wajah
        cv2.rectangle(mask, (x, y), (x + w, y + h), (255,255,255), -1)
        #cv2.imshow("Rectangular Mask", mask)

        
        # Menerapkan masking ke gambar
        masked = cv2.bitwise_and(images, images, mask=mask)
        cv2.imshow("Mask Applied to Image", masked)
        #cv2.imshow(str(w) + str(h) +"Mask Applied to Image", masked)

        # Konversi RGB ke HSV
        hsv = cv2.cvtColor(images,cv2.COLOR_BGR2HSV)
        
        # Parameter HSV
        lower_b = np.array([0, 10, 62])
        upper_b = np.array([26, 255, 255])
        
        # membuat mask HSV hasil dari pengubahan HSV
        mask_new = cv2.inRange(hsv, lower_b, upper_b)
        cv2.imshow('Mask', mask_new)

        #mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        #images = images*mask2[:,:,np.newaxis]
        
        # Menghitung seluruh jumlah pixel
        countpixel = np.sum(np.array(images) >= 200)
        #print('Number of pixels:', countpixel)

        # Menghitung pixel warna putih
        white_pixel = np.sum(images == 255)
        #print('Number of white pixels:', white_pixel)

        # Menghitung pixel warna hitam
        black_pixel = np.sum(img == 0)
        #print(str(w) + str(h) +'Number black of pixels:', black_pixel)
     
        # Deteksi mulut
        mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 5)
            
        # Deteksi hidung
        nose_detect = nose_cascade.detectMultiScale(gray, 1.5, 5)

            
        # Wajah terdeteksi tetapi mulut dan hidung tidak terdeteksi yang berarti orang tersebut memakai masker
        if(len(mouth_rects) == 0 and len(nose_detect) == 0 or black_pixel >= 200):
            label = "Menggunakan Masker"
            cv2.rectangle(images, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(images, label, (x, y- 10), font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)         
        else:
            for (mx, my, mw, mh) in mouth_rects:
                        
                if(y < my < y + h):
                    # Wajah dan Bibir terdeteksi tetapi koordinat mulut dan hidug berada dalam koordinat wajah yang 
                    # berarti prediksi bibir benar dan orang tidak memakai masker.
                    label = "Tidak Menggunakan Masker"
                    cv2.putText(images, label, (x, y- 10), font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)

                    #cv2.rectangle(img, (mx, my), (mx + mh, my + mw), (0, 0, 255), 3)
                    break

            cv2.rectangle(images, (x, y), (x + w, y + h),(0, 0, 255), 2)
                    
                    
          
# Menampilkan hasil Akhir Deteksi
cv2.imshow('Aminurachma: Mask Detection', images)
cv2.waitKey(0)
cv2.destroyAllWindows()