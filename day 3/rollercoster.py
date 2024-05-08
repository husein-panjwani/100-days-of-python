print("please take the ticet after verifications")
print("students get free tickets today")
height = int(input("enter your height: "))
bill = 0
if  height >= 180:
    print("you are eligable")
    student = input("are you a student? reply with y for a yes and n for a no: ")
    if student == "y" :
        bill = 0
    if student == "n":
        age = int(input("enter your age : "))
        if age<=12:
            bill = 50
        elif age <=18 :
            bill=100
        elif age >=55 and age<=60:
            bill = 0
        else:
            bill = 150
    
    want_photo=input("do you want a photo of yours during the ride it will be 50 extra? y or N: ")
    if want_photo == "y":
         bill = bill +50
else:
    print("you are not eligable")

print(f"your total bill = {bill}rs")