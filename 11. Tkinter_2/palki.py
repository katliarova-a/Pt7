from tkinter import *
from random import *
from tkinter import messagebox
window=Tk()
window.geometry("270x100")

n=20
def player():
    global n
    count_player=int(entr.get())
    entr.delete(0, END)
    n=n-count_player
    lbl.config(text=n*"|",font=("",26,"bold"))
    btn1["state"]="disable"
    btn2["state"]="normal"
    if n==1:
        messagebox.showinfo("Победа","Ура, вы победили!")
        btn1["state"] = "disable"
        btn2["state"] = "disable"

def computer():
    global n
    count_comp=randint(1,3)
    if n > 3:
        n=n-count_comp
        lbl.config(text=n * "|", font=("", 26, "bold"))
    else:
        count_comp=randint(1,n-1)
        n=n-count_comp
        lbl.config(text=n * "|", font=("", 26, "bold"))
    if n==1:
        messagebox.showinfo("Увы","Компьютер победил!")
        btn1["state"] = "disable"
        btn2["state"] = "disable"
    btn2["state"] = "disable"
    btn1["state"] = "normal"

Label(text="Выбери палочки 1-3").grid(row=0)
entr=Entry()
entr.grid(row=0,column=1)
lbl=Label(text=n*"|",font=("",26,"bold"))
lbl.grid(row=1,columnspan=2)
btn1=Button(text="Ход игрока",command=player)
btn1.grid(row=2)
btn2=Button(text="Ход компьютера",state="disable",command=computer)
btn2.grid(row=2,column=1)

window.mainloop()