h=input("enter height in m: ")
w=input("enter weight in kg: ")

h = float(h)
w = float(w)
bmi= w/(h**2)
bmi = round(bmi,2)
if bmi <= 18.5:
    print(f"your bmi is {bmi}, you are underweight")
elif bmi >18.5 and bmi<=25:
    print(f"your bmi is {bmi}, you are normal")
elif bmi> 25 and bmi<=30:
    print(f"your bmi is {bmi}, you are overweight")
elif bmi > 30 and bmi<=35:
    print(f"your bmi is {bmi}, you are obese")
elif bmi > 35 :
    print(f"your bmi is {bmi}, you are clinically obese")
