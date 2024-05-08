your_name=input("enter your name: ")
crush_name=input("Enter your crush name: ")

your_name = your_name.lower()
crush_name=crush_name.lower()

joint_name= your_name + crush_name

count_true= joint_name.count("t"and "r" and "u" and "e")
count_love= joint_name.count("l" and "o" and "v" and "e")

print (str(count_true) + str(count_love))
