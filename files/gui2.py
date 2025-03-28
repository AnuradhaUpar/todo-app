import FreeSimpleGUI as gui

from files.gui1 import button2, input2

label1=gui.Text("Enter feet")
label2=gui.Text("Enter in inches")
inputBox1=gui.InputText(tooltip="enter values")
inputBox2=gui.InputText(tooltip="enter values")
convert=gui.Button("Convert")
window=gui.Window("Convertor",layout=[[label1,inputBox1],[label2,input2],[convert]])
window.read()
window.close()

