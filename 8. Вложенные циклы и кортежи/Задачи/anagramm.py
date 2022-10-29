from random import choice
words=("попугай","хомяк","тушканчик","свинка","рыбки")
word=choice(words)
word_copy=tuple(word)
word_anagram=""
while len(word_copy)>0:
    letter=choice(word_copy)
    word_anagram+=letter
    indx=word_copy.index(letter)
    word_copy=word_copy[0:indx]+word_copy[indx+1:len(word_copy)]
print("anagram",word_anagram)
answer=input("Угадай слово по анаграмме")
if answer==word:
    print("Winner")
else:print("Loose")