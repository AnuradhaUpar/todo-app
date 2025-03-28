import FreeSimpleGUI as sg

label1=sg.Text("select file to compress :")
input1=sg.InputText(tooltip="file name")
button1=sg.FileBrowse("choose")

label2=sg.Text("select destination folder :")
input2=sg.Input(tooltip="folder name")
button2=sg.FolderBrowse("choose")

compress_button=sg.Button("compress")

window=sg.Window("select a file",layout=[[label1,input1,button1],[label2,input2,button2],[compress_button]])

window.read()
window.close()
