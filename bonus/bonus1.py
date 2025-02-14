User_input = input("add a new member:")

file = open("members.txt","r")
content = file.readlines()
file.close()

content.append(User_input + "\n")

file = open("members.txt","w")

content = file.writelines(User_input)
file.close()
