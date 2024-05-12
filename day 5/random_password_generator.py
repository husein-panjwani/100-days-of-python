import random

total_length = int(input("how long you want your password? "))
uppercase=int(input("how many uppercase you want ? "))
special= int(input("how many special characters you want? "))
numbers=int( input ("how many numbers you want in your password? "))

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers_list= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
password = []

for j in range (0, special):
    password.append(random.choice(special_characters))
    special= special-1
    total_length = total_length-1

for k in range (0,uppercase):
    password.append(random.choice(capital_letters))
    uppercase= uppercase-1
    total_length = total_length-1     

for l in range (0,numbers):
    password.append(random.choice(numbers_list))
    numbers = numbers-1
    total_length = total_length-1

for i in range (0, total_length):
    password.append(random.choice(small_letters))
    total_length = total_length-1

random.shuffle(password)

for i in password:
    print(i,end="")

