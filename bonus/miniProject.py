import random


User_input1 = int(input("Enter the lower bound: "))
User_input2 = int(input("Enter the upper bound: "))
result = random.randrange(User_input1,User_input2 + 1)
print(f"Random number between user input is : {result}")