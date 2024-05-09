import random

elements = ["rock","paper", "sissor"]
player= input("choose r for rock \nchoose p  for paper \nchoose s for sissor\n")

computer = random.choice(elements)

if player == "r" and computer == "rock" or player == "p" and computer == "paper" or player == "s" and computer == "sissor":
    print("itsa tie")
    print(f"computer choose {computer}")
elif player == "r"  :
    if computer == "paper":
        print ("you loose")
        print(f"computer choose {computer}")
    elif computer == "sissor":
        print ("you won")
        print(f"computer choose {computer}")
elif player == "p"  :
    if computer == "sissor":
        print ("you loose")
        print(f"computer choose {computer}")
    elif computer == "rock":
        print ("you won")
        print(f"computer choose {computer}")
elif player == "s"  :
    if computer == "paper":
        print ("you won")
        print(f"computer choose {computer}")
    if computer == "rock":
        print ("you loose")
        print(f"computer choose {computer}")

