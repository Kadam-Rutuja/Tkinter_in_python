import tkinter
from tkinter import *

w = Tk()

w.geometry("400x150+10+10")

chkb1 = Checkbutton(w,text="c")
chkb1.pack()

chkb2 = Checkbutton(w,text="c++")
chkb2.pack()

chkb3 = Checkbutton(w,text="java")
chkb3.pack()

w.mainloop()