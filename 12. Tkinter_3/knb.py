from tkinter import *
from random import randint
window=Tk()
window.title("play the game")
window.geometry("350x200")
window["bg"]="#CCCCCC"
Label(text="You choise:").grid(row=1, column=1)
lbl1=Label(text="Choise comp",font=("Comic Sans MS",16))
lbl1.grid(row=3, column=0, columnspan=3, pady=10)
lbl2=Label(text="",bg="#CCCCCC")
lbl2.grid(row=4, column=0, columnspan=3)

def play():
    btn1.configure(state="normal")
    btn2.configure(state="normal")
    btn3.configure(state="normal")
    btn_play.configure(state="disable")
    lbl1.configure(text="Выбор компьютера:")
    lbl2.configure(text="",bg="#CCCCCC")

def choise_user(argument):
    comp_choise=randint(1,3)
    btn1.configure(state="disable")
    btn2.configure(state="disable")
    btn3.configure(state="disable")
    btn_play.configure(state="normal")
    if argument=="к":
        if  comp_choise==1:
            lbl1.configure(text="Выбор компьютера: камень")
            lbl2.configure(text="Ничья", bg="orange")
        elif comp_choise==2:
            lbl1.configure(text="Выбор компьютера: ножницы")
            lbl2.configure(text="Вы выиграли", bg="green")
        else:
            lbl1.configure(text="Выбор компьютера: бумага")
            lbl2.configure(text="Вы проиграли", bg="red")
    elif argument == "н":
        if comp_choise == 1:
            lbl1.configure(text="Выбор компьютера: камень")
            lbl2.configure(text="Вы проиграли", bg="red")
        elif comp_choise == 2:
            lbl1.configure(text="Выбор компьютера: ножницы")
            lbl2.configure(text="Ничья", bg="orange")
        else:
            lbl1.configure(text="Выбор компьютера: бумага")
            lbl2.configure(text="Вы выиграли", bg="green")
    elif argument == "б":
        if comp_choise == 1:
            lbl1.configure(text="Выбор компьютера: камень")
            lbl2.configure(text="Вы выиграли", bg="green")
        elif comp_choise == 2:
            lbl1.configure(text="Выбор компьютера: ножницы")
            lbl2.configure(text="Вы проиграли", bg="red")
        else:
            lbl1.configure(text="Выбор компьютера: бумага")
            lbl2.configure(text="Ничья", bg="orange")

btn_play=Button(text="Play", command=play)
btn_play.grid(row=0, column=1, pady=10)
btn1=Button(text="камень",font=("Comic Sans MS",16),state="disable",command=lambda :choise_user("к"))
btn1.grid(row=2,column=0, padx=5)
btn2=Button(text="ножницы",font=("Comic Sans MS",16),state="disable",command=lambda :choise_user("н"))
btn2.grid(row=2,column=1, padx=10)
btn3=Button(text="бумага",font=("Comic Sans MS",16),state="disable",command=lambda :choise_user("б"))
btn3.grid(row=2,column=2, padx=5)
window.mainloop()