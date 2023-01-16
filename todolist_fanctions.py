FILE_PATH = '/home/elen/Projekty/Udemy/The Python Mega Course- Learn Python in 40 Days with 18 Apps/To_do_list/todo_text_file.txt'

def get_todos(filepath = FILE_PATH):
    with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines() 
    return todos_local

def write_todos(todos_arg, filepath = FILE_PATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(get_todos())