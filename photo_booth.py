# custom made buttons for tkinter
 
import tkinter as tk
 
 
root = tk.Tk()
 
def image(smp):
    img = tk.PhotoImage(file="red.png")
    img = img.subsample(smp, smp)
    return img
 
 
but = tk.Button(
    root,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    fg="yellow",
    activeforeground="pink",
    activebackground="white",
    font="arial 20",
    text="Click me",
    pady=10,
    # width=300
    )
 
img = image(2) # 1=normal, 2=small, 3=smallest
but.config(image=img)
but.pack()
 
 
root.mainloop()