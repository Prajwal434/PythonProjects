import FreeSimpleGUI as sg


label1 = sg.Text("Enter feet:")
input_text1 = sg.Input()

label2 = sg.Text("Enter inches:")
input_text2 = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label1,input_text1],[label2,input_text2],
                                             [convert_button]])
window.read()
window.close()