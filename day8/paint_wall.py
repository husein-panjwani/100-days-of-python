import math
def paint (height , width,coverage):
    cans_required = math.ceil((height * width)/coverage)
    # cans_required = round(cans_required)
    print(f"to paint the wall of {height}m and widht {width}m we need to buy {cans_required} cans of paint")

height = int(input("enter height "))
width = int(input("enter width "))
coverage =5

paint (height , width, coverage)