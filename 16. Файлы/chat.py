from tkinter import *
from tkinter import filedialog
window=Tk()
nam=Entry()
nam.grid(row=0, column=0)
text=Text( width=50)
text.grid(row=1,columnspan=2)
text2=Text( width=40, height=5)
text2.grid(row=2,columnspan=2)

def savefile():
    file=open("chat.txt","r+")
    s_file = file.read()  # чтение данных из файла
    text.delete(1.0,END)
    text.insert(1.0, s_file)  # запись данных в текстовое поле
    file.close()
    window.after(2000, savefile)

def entr():
    file = open("chat.txt", "a")
    s_file = nam.get() + ":    " + text2.get(1.0, END)
    file.write(s_file)
    file.close()
    text2.delete(1.0,END)

Button(text="Отправить",command=entr).grid(row=3,column=1)

savefile()
window.mainloop()