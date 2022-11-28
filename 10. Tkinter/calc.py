from tkinter import *
windows=Tk()
windows.geometry("350x200+500+300")
windows.title("Самый простой калькулятор")

def calc(arg):
    entr3.delete(0,END)
    if arg==1:
        entr3.insert(0,(int(entr1.get())+int(entr2.get())))
    if arg==2:
        entr3.insert(0,(int(entr1.get())-int(entr2.get())))
    if arg==3:
        entr3.insert(0,(int(entr1.get())*int(entr2.get())))
    if arg==4:
        entr3.insert(0,(int(entr1.get())/int(entr2.get())))

Label(text="Первое число").grid(row=0,columnspan=2)
Label(text="Второе число").grid(row=3,columnspan=2)
Label(text="Результат",bg='#FFC0CB').grid(row=1,column=2, columnspan=2)
entr1=Entry(bd=5)
entr2=Entry(bd=5)
entr3=Entry()
btn1=Button(text="+",width=5,command=lambda :calc(1))
btn2=Button(text="-",width=5,command=lambda :calc(2))
btn3=Button(text="*",width=5,command=lambda :calc(3))
btn4=Button(text="/",width=5,command=lambda :calc(4))

entr1.grid(row=1,column=0, columnspan=2,padx=20)
entr2.grid(row=4,column=0, columnspan=2)
entr3.grid(row=3,column=2, columnspan=2,padx=20)
btn1.grid(row=5,column=0,padx=10, pady=20)
btn2.grid(row=5,column=1,padx=10, pady=20)
btn3.grid(row=5,column=2,padx=10, pady=20)
btn4.grid(row=5,column=3,padx=10, pady=20)
windows.mainloop()