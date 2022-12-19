FILE_PATH = 'todo_text_file.txt'

def get_todos(filepath = FILE_PATH):
    with open(filepath, 'r') as file:
            todos_local = file.readlines() 
    return todos_local

def write_todos(todos_arg, filepath = FILE_PATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
