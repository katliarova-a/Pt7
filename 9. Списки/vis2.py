import random
words=[["м","а","м","а"],["п","а","п","а","й","я"],["б","а","б","а","к"]]
vis=["1","2","3","4","5"]
word_for_user=random.choice(words)
letter_for_user=[]
attempt=0
for i in range(len(word_for_user)):
    letter_for_user.append("_")
print("Угадай это слово", letter_for_user)
while "_" in letter_for_user:
    letter=input("Введи букву")
    if letter in word_for_user:
        print(letter, "есть в слове")
        while letter in word_for_user:
            indx= word_for_user.index(letter)
            letter_for_user[indx]=letter
            word_for_user.pop(indx)
        print(letter_for_user)
    elif letter not in word_for_user:
        print(letter, "в слове нет")
        print(vis[attempt])
        attempt+=1
        if attempt==5:
            print("game over")
            break

