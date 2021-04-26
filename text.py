import tkinter
from tkinter import *

w = Tk()

tx = Text(w,height=5,width=20,font='20')
tx.pack()

tx.insert(END,'Hello from Tkinter')

w.mainloop()