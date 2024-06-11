from art import logo

def add(num1 ,num2):
    return num1 + num2

def sub(num1 ,num2):
    return num1 - num2

def mul(num1 ,num2):
    return num1 * num2

def div(num1 ,num2):
    return num1 / num2


result = {
    "+" : add,
    "-": sub,
    "*": mul,
    "/": div,
    }

def calculator():
    print (logo)
    num1 = float(input("enter first number: "))
    for i in result:
         print (i)
    cont =1
    while cont == 1:
        symbol = input("pick one of the following operation: ")
        num2 = float(input("enter next number: "))

        function= result[symbol]
        answer = function(num1 , num2 )
        
        print(f"{num1} {symbol} {num2} = {answer}")
        choice= input(f"do u want to continue with {answer} ? y/n of s for a new start ")
        
        if choice == "y":
            num1 =answer
            cont = 1
        elif choice == "n":
            print("you have exited") 
            cont = 0
        elif choice == "s":
            count =0
            calculator()

calculator()