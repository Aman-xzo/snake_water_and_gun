import random
print("Welcome to snake, water & gun")



def game():

    result = ""
    u = ""
    c = ""

    user = int(input("Emter '1' for snake \nEnter '2' for water \nEnter '3' for gun :"))
    computer = random.randint(1,3)



    if user == computer:
        u = "and"
        c = "same"
        result = "die"

    elif user == 1 and computer == 2:
        u = "snake"
        c = "water"
        result = "win"

    elif user == 1 and computer == 3:
        u = "snake"
        c = "gun"
        result = "loss"

    elif user == 2 and computer == 1:
        u = "water"
        c = "snake"
        result = "loss"

    elif user == 2 and computer == 3:
        u = "water"
        c = "gun"
        result = "win"

    elif user == 3 and computer == 1:
        u = "gun"
        c = "snake"
        result = "win"

    elif user == 3 and computer == 2:
        u = "gun"
        c = "water"
        result = "loss"

    else:
        print("Error")

    print(f"your's {u} computer's {c}")
    print (f"--> {result}")





while True:
    usr = input("press 'Enter' for play or 'x' for stop :")

    if usr == "":
        game()

    elif usr == "x":
        break

    else:
        break





