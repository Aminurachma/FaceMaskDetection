import sys
import os
from tkinter import *
import tkinter
from tkinter_custom_button import TkinterCustomButton
import cv2
import tkinter.filedialog as tkFileDialog

window=Tk()

window.title("FaceMask Detection")
window.geometry('550x180')
window.configure(background='#FFFFFF')

def run():
    os.system('SkripsiAmi.py')
	
def run2():
    path = tkFileDialog.askopenfilename()
    # pastikan path file telah dipilih
    if len(path) > 0:
        image = cv2.imread(path)
    os.system('SkripsiAmiUpload.py '+ path)
 

label1 = Label(window, text="FACE MASK DETECTION", bg="white",font=("KTF-Roadstar", 17))
label1.place(relx=0.33, rely=0.04)

label3 = Label(window, text=" With Viola Jones Method", bg="white",font=("Century Gothic", 11))
label3.place(relx=0.33, rely=0.19)

label2 = Label(window, text="Aminurachma Aisyah - 17520001", bg="white", font=("Century Gothic", 10))
label2.pack(padx="4", pady="2", side="bottom")

from PIL import Image, ImageTk
imageee = ImageTk.PhotoImage(Image.open("coba.png").resize((130, 65)))
openfile = ImageTk.PhotoImage(Image.open("openfile.png").resize((130, 65)))

button_1 = TkinterCustomButton(text="Open Webcam", 
                                            bg_color=None,
                                            image=imageee,
                                            fg_color="#2874A6",
                                            hover_color="#5499C7",
                                            text_font=None,
                                            text_color="white",
                                            corner_radius=10,
                                            width=170,
                                            height=45,
                                            hover=True, command=run)
button_1.place(relx=0.33, rely=0.55, anchor=tkinter.CENTER)

button_2 = TkinterCustomButton(text="Open Files", corner_radius=10, 
                                            width=170,
                                            image=openfile,
                                            height=45,command=run2)
button_2.place(relx=0.66, rely=0.55, anchor=tkinter.CENTER)

from PIL import Image, ImageTk
logo1 = ImageTk.PhotoImage(Image.open("logo2.png").resize((60, 55)))
logo2 = ImageTk.PhotoImage(Image.open("logo.png").resize((40, 44)))

logo1 = TkinterCustomButton( fg_color="#FFFFFF",
                                        hover_color="#FFFFFF",
                                        image=logo1,  # <- add image (class PhotoImage)
                                        width=58,
                                        height=55,
                                        hover=True)
logo1.place(relx=0.05, rely=0.17, anchor=tkinter.CENTER)

logo2 = TkinterCustomButton( fg_color="#FFFFFF",
                                        hover_color="#808B96",
                                        image=logo2,  # <- add image (class PhotoImage)
                                        width=38,
                                        height=43,
                                        hover=True)
logo2.place(relx=0.94, rely=0.17, anchor=tkinter.CENTER)

window.mainloop()