from ConFunction import convert
import FreeSimpleGUI as sg



input_label1 = sg.Text("Enter feet")
input_box1 = sg.Input(key="feet")

input_label2 = sg.Text("Enter inches")
input_box2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("",key="output")

window = sg.Window("Convertor", layout=[[input_label1,input_box1],[input_label2,input_box2],
                                        [convert_button,output_label]])
while True:
    event,values =window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result}m",text_color="white")
    break
window.close()

