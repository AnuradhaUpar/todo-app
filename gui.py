import FreeSimpleGUI as gui
import function


label=gui.Text("Type in a to do")
input_box=gui.InputText(tooltip="Enter todo")
add_button=gui.Button("Add")

window=gui.Window("My to-do App" , layout=[[label],[input_box,add_button]])
window.read()
print("hello")
window.close()


