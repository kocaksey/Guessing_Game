import random

with open('game_words.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def word_check(word):
    flag =True
    if word =="":
        while flag:
            a = input("Please write a word: ")
            if not a =="":
                word = a
                break
    elif word == " ":
        while flag:
            a = input("Please write a word: ")
            if not a == " ":
                word = a
                break



    d=word.lower()
    return d

def entry_check(string_in):
    flag = True
    a=""
    if string_in =="1":
        a="1"
    elif string_in == "2":
        a = "2"
    else:
        while flag:
            a=input("Input should be '1' or '2' : ")
            if a == "1":
                a = "1"
                break
            elif a == "2":
                a ="2"
                break

    return a

flag = True
while flag:
    word = random.choice(lines)
    print("_ " * len(word))
    is_it = ""
    liste = []
    c = list(range(0, len(word)))
    a = random.choice(c)
    c.remove(a)

    command = input("\n 1-Give me a letter \n 2-I want to Guess \n")
    b=entry_check(command)


    if b == "1":

        m = "_" * (a) + word[a] + "_" * (len(word) - a - 1)
        print(m)

        for x in word:
            command = input("\n 1-Give me a letter \n 2-I want to Guess \n")
            b = entry_check(command)

            a = random.choice(c)
            liste.append(a)
            c.remove(a)

            list1 = list(m)
            list1[a] = word[a]
            m = ''.join(list1)

            if len(liste) == len(word):
                print("You failed!")
                print(f"The word was '{m}' ")
                break
            if not "_" in m:
                break

            if b == "1":
                print(m)
            if b == "2":
                break
    o =""
    if b == "2":
        is_it = input("Type the word: ")
        o = word_check(is_it)
    if o == word:
        print("\nCongratulations!\nYour score is " + str(len(c) + 1) + " !")
        command = input("\n 1-Continue.. \n 2-End Game..\n")
        b = entry_check(command)
        if b == "2":
            flag = False

    else:
        print("You Failed!")
        print(f"The word was '{word}' ")

        command = input("\n 1-Try Again.. \n 2-End Game..\n")
        b = entry_check(command)
        if b == "2":
            flag = False


