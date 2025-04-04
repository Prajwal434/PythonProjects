import  Functions
import FreeSimpleGUI as sg
import time

sg.theme("black")
clock = sg.Text('',key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=Functions.get_todos(),key="todos",
                     enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
Exit_button = sg.Button("Exit")



window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box,edit_button,complete_button],
                           [Exit_button]],
                   font=('Helvetica',12))

while True:
    event,values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    window["clock"].update(value=time.strftime("%b %d, %Y  %H:%M:%S"))
    print(event)
    print(values)

    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
             todo_to_edit = values['todos'][0]
             new_todo = values['todo']

             todos = Functions.get_todos()
             index = todos.index(todo_to_edit)
             todos[index] = new_todo
             Functions.write_todos(todos)
             window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit", font=("helvetica",20),text_color="white")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = Functions.get_todos()
                todos.remove(todo_to_complete)
                Functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("please select an item to delete", font=('helvetica',20))
        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break
window.close()

