def hangman(word):
    wrong = 0
    stages = ["",
              "________      ",
              "|             ",
              "|       |     ",
              "|       0     ",
              "|      /|\    ",
              "|      / \    ",
              "|             "
              ]
    rletters = list(word)
    board = ["___"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "___" not in board:
            print("Вы выиграли! Было загаданно слово:")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли! Было загадано слово:{}.".format(word))


import random
keys = ["голем", "футбол", "урок", "бутылка", "носок", "глаз"]
hangman(keys[random.randint(0, len(keys))])
