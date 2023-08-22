import random
while True:
    choices = ["rock", "paper","scissor"]
    computer = random.choice(choices)
    player = None 

    while player not in choices:
        player = input("Enter rock paper or scissor")

    if (player == computer):
        print("computer:" , computer)
        print("player:", player)
        print("IT'S A TIE")
    elif player == "rock":
        if computer == "scissor":
            print("computer:" , computer)
            print("player:", player)
            print("You win")
        if computer == "paper":
            print("computer:" , computer)
            print("player:", player)
            print("Computer win")
    elif player == "paper":
        if computer == "scissor":
            print("computer:" , computer)
            print("player:", player)
            print("Computer win")
        if computer == "rock":
            print("computer:" , computer)
            print("player:", player)
            print("You win")
    elif player == "scissor":
        if computer == "rock ":
           print("computer:" , computer)
           print("player:", player)
           print("Computer win")
        if computer == "paper":
           print("computer:" , computer)
           print("player:", player)
           print("You win")

    play_again= input("Do u wanna play again? Yes / no")

    if play_again != "yes":
      break
print("bye")