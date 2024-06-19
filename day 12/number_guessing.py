import random
from art import logo

print(logo)
print("welcome to number guesing game!")
print("i am thing of a number between 1  - 100 ")
difficulty = input("select dificulty level easy or hard? ")

number = random.randint(1, 100)

print (number)


def hard():
    attempts = 5
    win = 0
    for i in range (1,6):
        print(f"you have {attempts} attempts left")
        guess = int(input("make a guess: "))
        if guess == number:
            win = 1
            return win
            
        elif guess > number:  
            print("too high!")
            attempts -= 1
            
        elif guess < number:
            print ("too low!")
            attempts -= 1
    return win


def easy():
    attempts = 10
    win = 0
    for i in range (1,11):
        print(f"you have {attempts} attempts left")
        guess = int(input("make a guess: "))
        if guess == number:
            win = 1
            return win
    
        elif guess > number:  
            print("too high!")
            attempts -= 1
            
        elif guess < number:
            print ("too low!")
            attempts -= 1
    return win

if difficulty == "hard":
    win = hard()
    if win ==1:
        print("you won the game! good job!")
    else:
        print("you lost the game")

elif difficulty == "easy":
    win = easy()
    if win ==1:
        print("you won the game! good job!")
    else:
        print("you lost the game")

