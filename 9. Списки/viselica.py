import random
import os
words = [['п','а','й','т','о','н'],['ф','о','р','м','а','т'],['а','н','а','н','а','с'],['э','к','р','а','н']]
vis=["""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
"""]
words_user=random.choice(words)
flag=0
words_letter=[]
print(words_user)
for i in range(len(words_user)):
    words_letter.append("_")
print("Угадайте слово, вводя по одной букве", words_letter)
while "_" in words_letter:
    letter=input("Вводи букву")
    if letter in words_user:
        os.system('cls')
        print(letter, "есть в слове")
        while letter in words_user:
            ind = words_user.index(letter)
            words_letter[ind]=letter
            words_user[ind]="_"
        print(words_letter)
    elif letter not in words_user:
        os.system('cls')
        print(letter, "в слове нет")
        print(vis[flag])
        flag+=1
        if len(vis)==0:
            print("Конец игры")
            break
    elif letter in words_letter:
        print(letter, "уже было")
input("Для выхода введите Enter")