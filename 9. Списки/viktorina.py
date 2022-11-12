import random

qest=["Имя","Фимилия","Вазраст","Пол","Вес","Рост","Дети","Работа"]
ans=["На","Ко","29","ж","73","170","Поля","Есть"]
bal=0
while len(qest):
    qest_po=random.choice(qest)
    print(qest_po)
    i = qest.index(qest_po)
    qest.pop(i)
    ans_po=input()
    if ans_po==ans[i]:
        bal=bal+1
        print("good")
print(bal)
