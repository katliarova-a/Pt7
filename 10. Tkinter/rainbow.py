from tkinter import *
windows=Tk()
windows.title("Радужные кнопки")
windows.geometry("400x450")

def clik(arg):
    entr.delete(0,END)
    if arg==1:
        lbl.configure(text="Красный цвет")
        entr.insert(0,'#FF0000')
    elif arg==2:
        lbl.configure(text="Оранжевый цвет")
        entr.insert(0, '#FF8C00')
    elif arg==3:
        lbl.configure(text="Желтый цвет")
        entr.insert(0, '#FFFF00')
    elif arg==4:
        lbl.configure(text="Зеленый цвет")
        entr.insert(0, '#008000')
    elif arg==5:
        lbl.configure(text="Голубой цвет")
        entr.insert(0, '#00FFFF')
    elif arg==6:
        lbl.configure(text="Синий цвет")
        entr.insert(0, '#0000FF')
    elif arg==7:
        lbl.configure(text="Фиолетовый цвет")
        entr.insert(0, '#9400D3')

lbl=Label(text="Здесь будет название цвета",height=2)
entr=Entry(width=40,bd=10)
lbl.pack()
entr.pack()
btn1=Button(bg='#FF0000',width=40,height=2,command=lambda: clik(1) ).pack()
btn2=Button(bg='#FF8C00',width=40,height=2,command=lambda: clik(2)).pack()
btn3=Button(bg='#FFFF00',width=40,height=2,command=lambda: clik(3)).pack()
btn4=Button(bg='#008000',width=40,height=2,command=lambda: clik(4)).pack()
btn5=Button(bg='#00FFFF',width=40,height=2,command=lambda: clik(5)).pack()
btn6=Button(bg='#0000FF',width=40,height=2,command=lambda: clik(6)).pack()
btn7=Button(bg='#9400D3',width=40,height=2,command=lambda: clik(7)).pack()


windows.mainloop()