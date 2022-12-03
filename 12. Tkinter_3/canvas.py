from tkinter import *

root = Tk()
c = Canvas(width=700, height=500, bg='white')
c.focus_set()
c.pack()


ball = c.create_oval(50, 50, 65, 65, fill='green')

click=0
def moves(event):
    global click
    click += 1
    lbl["text"] = "Количество шагов: "+str(click)
    if event.keysym=="Up":
        c.move(ball, 0, -2)
    if event.keysym == "Left":
        c.move(ball, -2, 0)
    if event.keysym == "Right":
        c.move(ball, 2, 0)
    if event.keysym == "Down":
        c.move(ball, 0, 2)


c.bind('<Up>', moves)
c.bind('<Down>',moves)
c.bind('<Left>',moves)
c.bind('<Right>',moves)
lbl=Label(text="Считаем шаги")
lbl.pack()

root.mainloop()
