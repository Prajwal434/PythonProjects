import FreeSimpleGUI as sg

label = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")
compress_button = sg.Button("Compress")
window = sg.Window("Compress file", layout=[[label,input1,choose_button1],
                                                [label2,input2,choose_button2],
                                                 [compress_button]])
window.read()
window.close()