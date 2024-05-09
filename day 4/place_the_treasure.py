row1 = ["X","X","X"]
row2 = ["X","X","X"]
row3 = ["X","X","X"]

matrix = [row1,row2,row3]
print (f"{row1}\n{row2}\n{row3}")

treasure = input("where you want to put a treasure in the matrix? (row , coloum) ")
treasure = treasure.split(",")

treasure1= int(treasure[0])
treasure2= int(treasure[1])

matrix [treasure2 - 1] [treasure1 - 1] = "T"
print (f"{row1}\n{row2}\n{row3}")

                                