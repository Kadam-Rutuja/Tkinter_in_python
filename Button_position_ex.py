import tkinter
from tkinter import *

m = Tk()

redBtn = Button(m,text = "Red",fg = "red")
redBtn.pack( side = LEFT)

orangeBtn = Button(m,text = "Orange",fg = "orange")
orangeBtn.pack( side = RIGHT)

greenBtn = Button(m,text = "green",fg = "green")
greenBtn.pack( side = TOP)

yellowBtn = Button(m,text = "yellow",fg = "yellow")
yellowBtn.pack( side = BOTTOM)

m.geometry("200x200")

m.mainloop()