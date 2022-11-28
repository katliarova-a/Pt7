from tkinter import *
window=Tk()
window.title("Hello")
window.geometry("200x200")
window["bg"]="#F00356"
Label(text="What is your name").pack()
entr=Entry()
entr.pack()

def name():
    name=entr.get()
    privet.configure(text=name)

Button(text="click",command=name).pack()
privet=Label()
privet.pack()
window.mainloop()

