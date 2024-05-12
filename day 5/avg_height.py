age = input ("enter series od numbers: ")

age = age.split(" ")
# age = int(age)
sum = 0
count =0
for i in age:
    sum = sum + int (i)
    count = count+1

avg = int (sum)  / count
avg = round(avg)
print(f"average height is {avg}")

