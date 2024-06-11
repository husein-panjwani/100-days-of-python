

def leap (year):
    leap=0
    if year % 4==0 :
        leap = 1
        
        if year % 100 == 0 :
            leap = 0
        if year %400==0:
            leap = 1
        
    return leap

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

is_leap = leap(year) 

# print (is_leap)

# if is_leap == 1:
#     print(f"{year} is a leap year")
# elif is_leap ==0:
#     print(f"{year} is not a leap year")

def days_in_month(year,month):
    stage = 0
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     
    if is_leap ==1 and month == 2:
        month_days[1]= 29
        
    for i in month_days:
        index = i
        if stage == month-1:
            return index
        stage += 1
    
 
days = days_in_month(year, month)
print(days)