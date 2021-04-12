import sys
import os
from tkinter import *
import cv2
import tkinter.filedialog as tkFileDialog

window=Tk()

window.title("FaceMask Detection")
window.geometry('350x200')

def run():
    os.system('SkripsiAmi.py')
	
def run2():
    path = tkFileDialog.askopenfilename()
    # pastikan path file telah dipilih
    if len(path) > 0:
        image = cv2.imread(path)
    os.system('SkripsiAmiUpload.py '+ path)
 
label = Label(text="FACE MASK DETECTION WITH VIOLA JONES METHOD", fg="white", bg="black")
label.pack(side="top", fill="both", expand="yes", padx="10", pady="10")

btn = Button(window, text="Face Mask Detection with Webcam", command=run)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

btns = Button(window, text="Face Mask Detection with Upload File", command=run2)
btns.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

window.mainloop()