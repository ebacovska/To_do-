import todolist_fanctions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do list")
input_box = sg.InputText(tooltip="Entre todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = todolist_fanctions.get_todos(), key = "todos",
 enable_events = True, size = [45,10])

edit_buton = sg.Button("Edit")

window = sg.Window("My to-do list", 
            layout=[[label], [input_box, add_button], [list_box, edit_buton]],
            font = ("Helvetica", 20))

while True:
    event, test= window.read()
    print(1, event)
    print(2, test)
    print(3, test["todos"])
    if event == "Add":
        todos = todolist_fanctions.get_todos()
        new_todo = test["todo"] + "\n"
        todos.append(new_todo)
        window["todos"].update(values = todos)
        todolist_fanctions.write_todos(todos)
        
    
    elif event == "Edit":
        old_todo = test["todos"][0]
        new_todo = test["todo"]

        todos = todolist_fanctions.get_todos()
        index_of_change_itam = todos.index(old_todo)
        todos[index_of_change_itam] = new_todo  + "\n"
        todolist_fanctions.write_todos(todos)
        window["todos"].update(values = todos)
    elif event == "todos":
        window["todo"].update(value = test["todos"][0])
    elif event == sg.WIN_CLOSED:
        break
        

window.close()
        

