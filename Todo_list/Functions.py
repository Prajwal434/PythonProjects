FILEPATH = "todo.txt"



def get_todos(filepath = FILEPATH):
    """opens the file and reads the existing todos"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """write the todos in the text file"""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)