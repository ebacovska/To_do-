FILE_PATH = 'To_do_list.txt'

def get_todos(filepath = FILE_PATH):
    with open(filepath, 'r') as file:
            todos_local = file.readlines() 
    return todos_local
