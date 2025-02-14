New_password = input("Enter new password: ")
result=[]

if len(New_password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in New_password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False
for i in New_password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

print(all(result))

