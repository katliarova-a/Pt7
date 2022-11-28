from tkinter import *
window=Tk()
window.title("Кликер")
window.geometry("250x100")

sec=0
def stsec():
    global sec
    btn2.configure(state="normal")
    sec=sec+1
    if sec<10:
        window.after(1000,stsec)
        lbl.configure(text=sec)
    else:
        btn2.configure(state="disable")
        lbl.configure(text=("За "+str(sec)+" секунд количество нажатий "+str(click)))

click=0
def clickcount():
    global click
    click+=1
    btn2.configure(text=(click,"нажатий"))

lbl=Label(text="Жми на Старт и кликай быстрее",width=35)
lbl.grid(row=0)
btn1=Button(text="Старт",command=stsec)
btn1.grid(row=1)
btn2=Button(text="Нажимай",state="disable",command=clickcount)
btn2.grid(row=2)


window.mainloop()

