from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

window=Tk()
text=Text(width=40, height=15)
text.pack()
entr=Entry()
entr.pack()

file=open("viktorina.txt","r",encoding="utf-8")
line=file.readlines()
num_line=0

def main():
    global num_line
    if num_line<=len(line)-7:
        for i in range(num_line,num_line+2):
            text.insert(END, line[i])
        n = 1
        for j in range(num_line+2,num_line+6):
            text.insert(END, " "+str(n)+"  "+line[j])
            n=n+1
    elif num_line>len(line)-7:
        text.insert(1.0, "game over")

def answer():
    global num_line
    if num_line<=len(line)-7:
        ans=entr.get()
        ans_correct=int(line[num_line+6])
        if int(ans)==ans_correct:
            messagebox.showinfo("Верно","Вы умный однако!")
        else:
            messagebox.showinfo("УПС","Бывают в жизни огорчения")
        text.delete(1.0,END)
        entr.delete(0, END)
        num_line+=+7
        main()
    else:
        messagebox.showinfo("Конец", "Вы решили все загадки")

file.close()
main()
Button(text="принять ответ",command=answer).pack()
window.mainloop()