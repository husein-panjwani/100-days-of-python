import os
from blind_auction_art import logo

print (logo)
print ("welcome to the silent auction ")
bidder={}
plan =1
def winner():
    winner = ""
    prize = 0
    for i in bidder:
        if prize < bidder[i]:
            prize = bidder[i]
            winner = i
    print (f"{winner} bid for {prize} which was highest therefore {winner} won this auction")
    
while plan == 1:
    name = input("enter the name of bidder: ")
    bid = int(input("enter the bid $"))
    bidder[name] = bid
    name = ""
    choice = input("are there any other bids? Y/N ")
    if choice == "y":
        os.system("cls")
    else :
        plan = 0
        os.system("cls")
        winner()
    