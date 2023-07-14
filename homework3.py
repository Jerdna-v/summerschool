# *задачите да се решат со помош на numpy и random
# Задача 1:
# Да се напише функција којашто ќе генерира пасворд. Пасвордот треба да ги исполнува следниве услови:
# - барeм две големи букви
# - барем една мала буква
# - барем 1 цифра
# - барем 1 карактер
# - должина >= 8
import random
import string

import numpy

alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(random.choice(alphabet) for i in range(8))
    if (sum(c.islower() for c in password) >=1 and sum(c.isupper() for c in password) >=2 and sum(c.isdigit() for c in password) >=1): break
print(password)
# Задача 2: Напишете програма која овозможува на корисникот да игра игра на rock-paper-scissors против компјутерот.
# Компјутерот треба да случајно избере камен, ножици или хартија и да го спореди со изборот на корисникот. Да се
# одреди победникот или да се објави дека има исти резултати според правилата на играта.

user=input("Rock, Paper, Scissors: ")
AI = random.choice(numpy.array(["rock", "paper", "scissors"]))
print(AI)
if user.lower()==AI: print("Draw")
else:
    if (user.lower()=="rock" and AI=="scissors") or (user.lower()=="paper" and AI=="rock") or (user.lower()=="scissors" and AI=="paper"):print("User won")
    elif user.lower() in ["rock", "paper", "scissors"]: print("AI won")
    else: print("Invalid input")


# Задача 3: Напишете програма која овозможува на корисникот да игра игра на Hangman. Програмата треба случајно да
# избере збор од претходно дефинирана листа а потоа корисникот треба да погоди букви за да го заврши зборот.
# Прикажете го напредокот на зборот, погодените букви и бројот на преостанати обиди. Корисникот треба да има
# ограничен број на обиди пред да губи играта.

word=random.choice(numpy.array(["rock", "paper", "scissors"]))
print(word)
empty="".join(["_" for x in range(len(word))])
lives=5
while True:
    if empty==word:
        print("You won")
        break
    if lives==0:
        print("You lost")
        break
    print(lives)
    print(empty)
    user_inp=input("Guess: ")
    if user_inp not in word:
        lives-=1
        continue
    else:
        counter = 0
        while counter < len(word):
            if user_inp not in word[counter:]:break
            if user_inp == word[counter]:
                empty = list(empty)
                empty[counter]=user_inp
                empty = "".join(empty)
            counter += 1