import random
import word_database


# with open('game_words.txt') as file:
#     lines = file.readlines()
#     lines = [line.rstrip() for line in lines]
#     print(lines)

while True:
    word = random.choice(word_database.word_pool)
    print("_ " * len(word))
    is_it = ""
    liste = []
    c = list(range(0, len(word)))
    a = random.choice(c)
    c.remove(a)

    command = input("\n 1-Give me a letter \n 2-I want to Guess \n")

    if command == "1":
        m = "_" * (a) + word[a] + "_" * (len(word) - a - 1)
        print(m)

    if command == "1":
        for x in word:
            command = input("\n 1-Give me a letter \n 2-I want to Guess \n")
            # a = random.randint(0, len(word)-1)
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

            if command == "1":
                print(m)
            if command == "2":
                break

    if command == "2":
        is_it = input("Type the word: ")
    if is_it == word:
        print("\nCongratulations!\nYour score is " + str(len(c) + 1) + " !")
        x = input("\n 1-Continue.. \n 2-End Game..\n")
        if x == "2":
            break

    else:
        print("You Failed !")
        print(f"The word was '{word}' ")

        y = input("\n 1-Try Again.. \n 2-End Game..\n")
        if y == "2":
            break
