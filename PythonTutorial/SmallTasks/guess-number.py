from random import randint

keep_going = "y"
while keep_going == "y":
    number = randint(0, 100)
    guess = -1

    while number != int(guess):
        guess = input("Give a number (0-100): ")
        if guess == "":
            print("Type proper value")
            guess = -1
        elif int(guess) > number:
            print("Too big!")
        elif int(guess) < number:
            print("Too small!")
    print("You won!")
    keep_going = input("Once more? (y/n) ")
print("Thanks for playing :)")