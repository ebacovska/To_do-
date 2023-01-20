import todolist_fanctions
import PySimpleGUI as sg
import time

sg.theme("DarkBlue4")

clock = sg.Text("", key="clock_label")
label = sg.Text("Type in a to-do list")
input_box = sg.InputText(tooltip="Entre todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = todolist_fanctions.get_todos(), key = "todos",
enable_events = True, size = [45,10])
complete_bonut = sg.Button("Complete")
exit_buton = sg.Button("Exit")


edit_buton = sg.Button("Edit")

window = sg.Window("My to-do list", 
            layout=[[clock], 
             [label],
             [input_box, add_button],
             [list_box, edit_buton, complete_bonut],
             [exit_buton]],
             
            font = ("Helvetica", 20))

while True:
    event, test= window.read(timeout = 10)
    window["clock_label"].update(value=time.strftime(("%b %d, %Y %H:%m:%S")))
    # print(1, event)
    # print(2, test)
    # print(3, test["todos"])
    
    if event == "Add":
        todos = todolist_fanctions.get_todos()
        new_todo = test["todo"] + "\n"
        todos.append(new_todo)
        window["todos"].update(values = todos)
        todolist_fanctions.write_todos(todos)
        
    
    elif event == "Edit":
        try:
            old_todo = test["todos"][0]
            new_todo = test["todo"]

            todos = todolist_fanctions.get_todos()
            index_of_change_itam = todos.index(old_todo)
            if "\n" in test["todo"]:
                todolist_fanctions.write_todos(todos)
                window["todos"].update(values = todos)
            else:
                todos[index_of_change_itam] = new_todo  + "\n"
                todolist_fanctions.write_todos(todos)
                window["todos"].update(values = todos)
        except IndexError:
            sg.popup("please select a item first",font = ("Helvetica", 20))
    elif event == "Complete":
        try:
            todo_to_complete = test["todos"][0]
            todos = todolist_fanctions.get_todos()
            todos.remove(todo_to_complete)
            todolist_fanctions.write_todos(todos)
            window["todos"].update(values = todos)
            window["todo"].update(value = "")
        except IndexError:
            sg.popup("please select a item first",font = ("Helvetica", 20))
    elif event == "todos":
        window["todo"].update(value = test["todos"][0])

    elif event == "Exit":
        break
    elif event == sg.WIN_CLOSED:
        break
        

window.close()
        

