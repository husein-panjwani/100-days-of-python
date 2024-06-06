import math

def prime_numer(number):
    prime = 0
    divisible = 0
    for i in range (2,number):
        if number % i== 0:
            prime =1
            divisible = i
            break
        else:
            prime = 0
    
    if prime == 0:
        print("it's a prime number")
    else:
        print("its not a prime number")
        print(f"{number} is divisible by {divisible}")


number = int(input("Enter a number : "))

prime_numer(number)