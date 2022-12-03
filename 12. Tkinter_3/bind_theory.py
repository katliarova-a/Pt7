from tkinter import *
window=Tk()
window.geometry("400x400")
lbl=Label(text="text")
lbl.pack()
lbl2=Label(text="text")
lbl2.pack()

def fun1(event):
    lbl.configure(text="Left")

def fun2(event):
    lbl.configure(text="Right")

def move(event):
    x=event.x
    y=event.y
    lbl2.configure(text="Coords"+str(x)+","+str(y))

def show_key(event):
    window.title(str(event))

lbl.bind("<Button-1>",fun1)
lbl.bind("<Button-3>",fun2)
window.bind("<Motion>",move)
window.bind("<Key>",show_key)
window.mainloop()