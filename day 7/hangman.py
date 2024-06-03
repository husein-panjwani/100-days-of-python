import random
import os
from hangman_word import word_list
from hangman_art import logo ,stages 


print(logo)
choice = random.choice(word_list)
print (choice)
length = len(choice)

list = []
for i in range(length):
    list.append("_")
life = 6
print (list)
end =False
while not end:
    guess = input("guess a word: ").lower()
    
    if guess in list:
        print ("you already choose the word")
    for i in range(length):
        j=choice[i]
        if j==guess:
            list[i] = guess 

          
        
    if guess not in choice:
        os.system("cls")
        print (f"try again you guessed {guess} which is not in the word you loose a life ")
        life -= 1
        print(stages[life])
        
    print(list)
    
    if "_" not in list:
        end = True
        print("you win")
    elif life == 0:
        end = True
        print(f"you loose the word was {choice}")

