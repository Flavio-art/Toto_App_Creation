#Import the necessary functions from modules
from functions import get_todo,write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is " + now)

while True:
    #Get user input and strip space characters from it
    user_action = input("Input add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action.split()[0] or 'new' in user_action.split()[0]:
        todo = user_action[4:]

        todos = get_todo()

        todos.append(todo + "\n")

        write_todos(todos)

    elif 'show' in user_action.split()[0] or 'display' in user_action.split()[0]:
        todos = get_todo()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif 'exit' in user_action.split()[0]:
        break

    elif 'edit'  in user_action.split()[0]:
        try:
            number = int(user_action[5:])

            todos = get_todo()

            new_input = input("What do you want to change it to? ")
            todos[number - 1]  = new_input + "\n"

            write_todos(todos)

        except ValueError:
            print("Invalid input. Please try again entering a number after edit.")
            continue

    elif 'complete' in user_action.split()[0]:
        try:
            number = int(user_action[9:])

            todos = get_todo()

            index = number - 1
            todo_to_remove = todos[index].strip()
            todos.pop(index)

            write_todos(todos)

            print(f"Todo {todo_to_remove} is removed from the list.")

        except IndexError:
            print("Invalid input. Please enter a valid index.")
            continue
    else:
        print("Command is not recognized. Please try again.")

print ('Bye!')
