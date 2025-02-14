name = "What is  your name ?"

while True:
    Name = input(name)
    print(Name.capitalize())
new_todos = []
            for item in todos:
                new_item = item.strip("\n")
                new_todos.append(new_item)