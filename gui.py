import PySimpleGUI as sg
import HerbManager
import main

herbManager = HerbManager.HerbManager()

layout = [
    [sg.Text("Herb Inventory")],
    [sg.Button("Herb Create")],
    [sg.Button("Add")],
    [sg.Button("Delete")],
    [sg.Text(herbManager.herb_dictionary)]
    ]

window = sg.Window("Herb Inventory", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Herb Create":
       
        herbManager.create_herbs()
    elif event == "Add":
        print("Herb Create")
    elif event == "Delete":
        print("Delete")



window.close()

#New window for create herb and edit herb?? Perhaps same window with a back button or smth smth.....
#Add List of Herbs on the side of the home page