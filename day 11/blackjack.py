import random
import os
from art import logo

print(logo)
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def computer(deck):
    computer_hand=[]
    for i in range (0,2):
        computer_hand.append(random.choice(deck))
    return computer_hand

def player(deck):
    player_hand= []
    for i in range (0,2):
        player_hand.append(random.choice(deck))
    return player_hand

def user_blackjack(player):
    user_blackjack= 0
    if 11 in player and 10 in player:
        user_blackjack = 1
    return user_blackjack

def comp_blackjack(computer):
    comp_blackjack = 0
    if 11 in computer and 10 in computer:
        comp_blackjack = 1
    return comp_blackjack
    
def player_total(player):
    sum =0
    for i in range(len(player)):
        sum += player[i]
    return sum

def computer_total(computer):
    sum=0
    for i in range(len(computer)):
        sum += computer[i]
    return sum    

def ace(both,sum):
    if 11 in both and sum >21:
        sum -= 10
    return sum
repeat =0
while repeat ==0:
    comp_hand = computer(deck)
    print (f"dealer cards are {comp_hand[0]}")

    user_hand = player(deck)
    print (user_hand)
    
    u_blackjack = (user_blackjack(user_hand))
    c_blackjack = comp_blackjack(comp_hand)
    
    if u_blackjack ==1 and c_blackjack == 1:
        print("its a black jack for dealer as well/ndealer wins")
    elif u_blackjack ==1 :
        print("you win its a blackjack")

    comp_total = computer_total(comp_hand)
    user_total = player_total(user_hand)
    user_total = ace(user_hand,user_total)
    comp_total = ace(comp_hand, comp_total)
    if user_total>21:
        print(f"its a bust you lose")
    else :
        card = "y"
        while card == "y":
            if user_total>21:
                print(f"its a bust you lose")
                card = "n"
                
            else:
                card = (input("do you want to hit or stand ? (y/n)"))
                if card == "y":
                    user_hand.append(random.choice(deck))
                    user_total += user_hand[-1]
                    print(user_hand)
                else :
                    card = "n"
                    if c_blackjack == 1 and u_blackjack == 0:
                        print("its a blackjack dealer wins")
                    print(comp_hand)
        
        while comp_total < 17 :
                comp_hand.append(random.choice(deck))
                comp_total += comp_hand[-1]
        print(comp_hand)

    if comp_total == user_total and user_total<21 and comp_total <21 :
        print (f"its a draw you toatl was {user_total}")
    elif user_total <=21 and user_total>comp_total:
        print(f"your total {user_total} dealer total is {comp_total} \n youwin")
    elif comp_total > 21 and user_total<21:
        print(f"dealer busts your win")
    elif comp_total > user_total and comp_total < 21 and user_total<21:
        print (f"you lose your total was {user_total}\n computer wins with a total of {comp_total}")
    # else :
    #     print (f"you lose your total was {user_total}\n computer wins with a total of {comp_total}")
    
    if input("do you want to play a new game? (y/n):")== "y":
        os.system("cls")
        repeat = 0
    else : repeat = 1