import functions
import FreeSimpleGUI as Sg

label = Sg.Text('Type in a To-Do')
input_box = Sg.InputText(tooltip='Enter To-Do',
                         key='todo',)
add_button = Sg.Button('Add')
list_box = Sg.Listbox(values=functions.get_todo(),
                      key='todos',
                      enable_events=True,
                      size=[45,10])
edit_button = Sg.Button('Edit')

window = Sg.Window('My To-Do App',
                   layout = [[label],
                             [input_box,add_button],
                             [list_box,edit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window['todos'].update(todos)
        case "todos":
            todos = window['todo'].update(value=values['todos'][0])
        case Sg.WIN_CLOSED:
            break
window.close()

