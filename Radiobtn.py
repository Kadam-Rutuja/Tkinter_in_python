import tkinter
from tkinter import *

w = Tk()

w.geometry("300x200")

rb = Radiobutton(w,text='select 1',bg='skyblue')
rb.pack()

rb = Radiobutton(w,text='select 2',bg='skyblue')
rb.pack()

w.mainloop()