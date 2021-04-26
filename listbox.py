import tkinter
from tkinter import *

w = Tk()

w.geometry("300x200")

lb = Listbox(w,bg='red')

lb.insert(1,'Demo 1')
lb.insert(2,'demo 2')
lb.insert(3,'demo 3')
lb.insert(4,'demo 4')

lb.pack()

w.mainloop()