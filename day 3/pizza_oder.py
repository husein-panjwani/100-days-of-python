size= input("what size you want your pizza S, M, L? ")
peporoni = input("do u want peperoni? ")
cheese = input("do you want extra cheese? ")

bill = 0

if size == "S":
    bill = 15
    if peporoni == "y":
        bill += 2
        if cheese == "y":
            bill += 1
elif size == "M":
    bill = 20
    if peporoni == "y":
        bill += 3
        if cheese == "y":
            bill += 1
elif size == "L":
    bill = 25
    if peporoni == "y":
        bill += 3
        if cheese == "y":
            bill += 1
            
print(f"total bill = ${bill}")