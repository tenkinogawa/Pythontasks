import random as rn

keep_going = "y"
while keep_going == "y":
    p1 = input("Rock, paper, scissors: ").lower()
    while p1 != "rock" and p1 != "paper" and p1 != "scissors":
        p1 = input("Wrong name. Try again.\nRock, paper, scissors: ").lower()

    p2 = rn.randint(0,2)

    if p2 == 0:
        p2 == "rock"
    elif p2 == 1:
        p2 = "paper"
    else:
        p2 = "scissors"

    print ("Computer choice: " + p2)

    if p1 == p2:
        print("It's a tie")
    elif p1 == "paper":
        if p2 == "rock":
            print("Player 1 wins")
        elif p2 == "scissors":
            print("Player 2 wins")
    elif p1 == "rock":
        if p2 == "scissors":
            print("Player 1 wins")
        elif p2 == "paper":
            print("Player 2 wins")
    elif p1 == "scissors":
        if p2 == "paper":
            print("Player 1 wins")
        elif p2 == "rock":
            print("Player 2 wins")
    else:
        print("Wrong input")
    keep_going = input("Once again (y/n): ")
