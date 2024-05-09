import random

name = input("enter the names of people seprated by ,: ")
name = name.split (",")

length= len(name)

person = random.randint(0, length - 1)

print(f"{name[person]} has to pay bill")
print (person)

