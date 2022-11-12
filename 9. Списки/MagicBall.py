from tkinter import *
from random import choice

def clicked():
    lbl.configure(text = choice(["Да","Нет","Возможно","Действуй","Не сегодня","Увы"]))


window = Tk()
window.title("Добро пожаловать!")
window.geometry('500x200')

lbl = Label(window, text="Задайте свой вопрос",font=("Arial Bold", 16))
txt = Entry(window,width=30)
btn = Button(window, text="Нажми, чтобы узнать ответ", command=clicked)

lbl.pack()
txt.pack()
btn.pack()
window.mainloop()