import PySimpleGUI as sg

layout = [
    [sg.Text("Herb Inventory")],
    [sg.Button("Herb Create")],
    [sg.Button("Add")],
    [sg.Button("Delete")]
    ]

window = sg.Window("Herb Inventory", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Herb Create":
        print("Herb Create")
    elif event == "Add":
        print("Herb Create")
    elif event == "Delete":
        print("Delete")



window.close()