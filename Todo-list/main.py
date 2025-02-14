def get_todos():
    with open('todo.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local



while True:
    User_action = input("type add, show, edit, complete or exit: ")
    User_action = User_action.strip()

    
    if User_action.startswith("add"):
          todo = User_action[4:]

          todos = get_todos()


          todos.append(todo + '\n') # This appends the input correctly

          with open("todo.txt","w") as file:
               file.writelines(todos)


    elif User_action.startswith("show"):
          todos = get_todos()



          for index,item in enumerate(todos):  # Iterate through all items in the list
                row = f"{index + 1}.{item}"
                row = row.strip("\n")
                print(row)


    elif User_action.startswith("edit"):
          try:


            number = int(User_action[4:])

            number = number - 1
            print(number)
            
            todos = get_todos()

          
            
            new_todo = input("enter new todo:")
            todos[number] = new_todo + '\n'

            with open("todo.txt", "w") as file:
              file.writelines(todos)
          except ValueError:
              print("your command is not valid")
              continue






    elif  User_action.startswith("complete"):
        try:
            number = int(User_action[9:])
            index = number-1


            

            todos = get_todos()



            
            Todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            

            with open("todo.txt", "w") as file:
              file.writelines(todos)
          
            message = f"todos {Todo_to_remove} is removed from the todo-list"
              
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue



    elif  User_action.startswith("exit"):
            break
    else:
         print("command is not valid")

print("bye!")
