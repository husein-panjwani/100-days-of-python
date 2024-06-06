from ceaser_art import logo 
alpha= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(text,shift,call):
    if call == "decrypt":
            shift *= -1  
    end_text = ""    
    temp = ""
    for i in text:
        temp = i 
        if temp in alpha:
            temp = alpha.index(temp)+shift
            temp = alpha[temp]
            end_text += temp
        else:
            end_text += temp
    print(f"your {call}ed text is: {end_text}") 

cont = 1

print(logo)
while cont == 1:
    
    call = input("do u want to encrypt or decrypt?: ")
    text = input(f"enter a text to {call}: ").lower()
    shift = int(input("enter a shift value: "))
    shift = shift % 26 
    ceaser(text,shift,call)
    
    user= input("do you want to continue? (y/n): ")
    if user == "y":
        cont =1
    elif user =="n":
        cont = 0

