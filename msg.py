import tkinter
from tkinter import *

w = Tk()

w.geometry("300x200")

msg ='Hello from Tkinter'

i = Message(w,text=msg,bg='yellow',font='60')
i.pack()

w.mainloop()