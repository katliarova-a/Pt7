from tkinter import *
import random
window=Tk()
lbl=Label()
lbl.pack()

def open_file():
    global line
    file = open("number.txt")  # открытие выбранного файла
    line = file.readlines()
    for i in range(0,len(line)):
        text.insert(END, line[i])
    file.close()  # закрытие файла

def save_file():
    file = open("number.txt", "w")
    s_file =text.get(1.0, END)
    file.write(s_file)
    file.close()

def go():
    save_file()
    global line
    ch=random.choice(line)
    print(ch)

text = Text(width=20, height=7)
text.pack(side=LEFT)
Button(text="Кликай на удачу соседа", command=go).pack()
open_file()
window.mainloop()
