score = input("enter scores")
score = score.split()

high = 0

for i in score :
    if int(i) > high:
        high = int(i)

print(f"highest score is {high}")
