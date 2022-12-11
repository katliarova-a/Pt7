from tkinter import *
from random import randint
window=Tk()
canvas=Canvas(width=400,height=400,bg="white")
foot=Canvas(width=400,height=100,bg="orange")
canvas.focus_set()
canvas.pack()
foot.pack()
img=PhotoImage(file="box2.png")
img=img.subsample(20,20)

count=0
def go():
    canvas.delete(ALL)
    x=randint(40,360)
    y=randint(40,360)
    print(x,y)
    can_image2=canvas.create_image(x,y,image=img)
    canvas.tag_bind(can_image2,'<Button-1>',click)
    window.after(500,go)

def click(event):
    global count
    count+=1
    foot.delete(ALL)
    foot.create_text(80,30,text=str(count),font="Arail 26")

go()

window.mainloop()
