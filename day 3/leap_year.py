year = int(input("enter year to check leap year"))

leap=0

if year % 4==0 :
    leap = 1
    # print(leap)
    if year % 100 == 0 :
     leap = 0
     if year %400==0:
         leap = 1
    #  print(leap)

if leap == 1:
    print(f"{year} is a leap year")
elif leap ==0:
    print(f"{year} is not a leap year")