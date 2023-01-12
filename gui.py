import todolist_fanctions
import PySimpleGUI as sg

label = sg.Text("Tipe in a to-do list")
input_box = sg.InputText(tooltip="entre todo")


window = sg.Window("My to-do list", layout=[[label], [input_box]])
window.read()
window.close()