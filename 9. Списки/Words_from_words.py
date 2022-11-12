from random import choice
from termcolor import colored
import os
words = ["пайтон","телефон","список","формат"]
answer = [["тон","пано","нота"],["фон","флот","енот","лот"],["сок","пик"],["форма","том","рота","фарт","фора","март"]]
list_answer_user=[]
name_1 = input("Как можно к вам обращаться?")
yes_no = "да"
coin=0
while yes_no == "да":
    print(name_1, ", поиграм в игру? да\нет")
    yes_no = input()
    if yes_no == "нет":
        break
    else:
        os.system('cls')
        rand_word = choice(words)
        print("Вам дано слово \033[35m",rand_word," \033[0m \n Составьте как можно больше слов из него \n Когда закончатся идеи, напиши 'сдаюсь'")
        answer_user = ""
        while answer_user!="сдаюсь":
            answer_user=input()
            ind = words.index(rand_word)
            if answer_user in answer[ind]:
                print(colored("Отлично","green"))
                list_answer_user.append(answer_user)
                coin+=len(answer_user)
                answer[ind].remove(answer_user)
                if len(answer[ind])==0:
                    print(name_1,colored(", Вы гений","blue"))
            elif answer_user=="сдаюсь":
                break
            elif answer_user in list_answer_user:
                print(colored("Такое слово уже было","yellow"))
            elif answer_user not in answer[ind]:
                print(colored("Такого слова я не знаю \n Давай другое","red"))
    print(colored("Ваш результат","purpure"))
    print("Составленные слова:",list_answer_user,"\n Количество баллов:",coin)
input("Для выхода введите Enter")