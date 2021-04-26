import tkinter
from tkinter import *

w = Tk()

b=Button(w,text="This Is Button",bg='red')
b.place(x=100,y=50)

w.title('my page')

w.geometry("300x200+100+200")

w.mainloop()