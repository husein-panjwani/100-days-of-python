print("welcome to tip calculator")
total = input("please enter your toatl bill:")
total=float(total)
tip_percent= int(input("please enter your tip percents: "))

total_bill= ((tip_percent /100) * total ) + total   
total_bill= round(total_bill,2)
total_split=int(input("please enter how many people u want to split the bill: "))

per_person=(total_bill/total_split)
print(f"your total bill is {total_bill} and each of you have to pay {per_person}")