import functions
import FreeSimpleGUI as Sg
import time

Sg.theme('Dark Blue 2')

clock = Sg.Text('', key = 'clock')
label = Sg.Text('Type in a To-Do')
input_box = Sg.InputText(tooltip='Enter To-Do',
                         key='todo',)
add_button = Sg.Button('Add')
list_box = Sg.Listbox(values=functions.get_todo(),
                      key='todos',
                      enable_events=True,
                      size=[45,10])
edit_button = Sg.Button('Edit')
complete_button = Sg.Button('Complete')

exit_button = Sg.Button('Exit')


window = Sg.Window('My To-Do App',
                   layout = [[clock],
                             [label],
                             [input_box,add_button],
                             [list_box,edit_button,complete_button],
                             [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todos'].update(todos)
            except IndexError:
                Sg.popup("Please enter a valid input", font=('Helvetica', 12))
        case ("Complete"):
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todo()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup("Please enter an input", font=('Helvetica', 12))

        case "Exit":
            break
        case "todos":
            todos = window['todo'].update(value=values['todos'][0])
        case Sg.WIN_CLOSED:
            break
window.close()

