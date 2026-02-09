FILEPATH = "files/todos.txt"

def get_todo(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Write a list of to-do items to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)