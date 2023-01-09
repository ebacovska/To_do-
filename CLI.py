import todolist_fanctions
import time


now = time.strftime("%b %d, %Y %H:%m:%S")
print("It is: " + now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

  

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = todolist_fanctions.get_todos()

        todos.append(todo + "\n")

        todolist_fanctions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = todolist_fanctions.get_todos()


        for index, item in enumerate(todos):
            item = item.translate({ord('\n'): None})
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            
            number = number - 1

            todos = todolist_fanctions.get_todos()

            new_todo = input("Entre a new todo: ")      
            todos[number] = new_todo + "\n"

            todolist_fanctions.write_todos(todos)

        except ValueError:
            print('It is not valide input')
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todolist_fanctions.get_todos()

            todo_to_remove = todos[number - 1].strip('\n')

            todos.pop(number-1)

            todolist_fanctions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed fromthe list"
            print(message)
        
        except IndexError:
            print('There is nothink with thet number')
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("try it again")