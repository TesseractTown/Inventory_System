import PySimpleGUI as sg
import HerbManager
import main

herbManager = HerbManager.HerbManager()

class GuiLayouts:
    def home_page_layout():
        layout = [
            [sg.Text("Herb Inventory")],
            [sg.Button("Herb Create"), sg.Button("Add"),sg.Button("Delete")],
            [sg.Button("Debug")],
           
            [sg.Text (print (herbManager.herb_dictionary.keys, herbManager.herb_dictionary.values))]
        ]

        GuiLayouts.window = sg.Window("Herb Inventory", layout, finalize=True)

        while True:
            event, values = GuiLayouts.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Herb Create":
       
                herbManager.create_herbs()
                #GuiLayouts.window[GuiLayouts.home_page_layout()].update(herbManager.herb_dictionary.keys)

            elif event == "Add":
                GuiLayouts.herb_edit_layout()

            elif event == "Delete":
                print("Delete")
            elif event == "Debug":
               herbManager.get_dict_keys() 
        
    def herb_edit_layout():

        GuiLayouts.herb_names = [
            herbManager.get_dict_keys()
        ]

        GuiLayouts.list_box = sg.Listbox(GuiLayouts.herb_names,
                                         size= (20,4),
                                         font=("Calibri", 14),
                                         expand_y=True,
                                         enable_events=True,
                                         key="list")

        layout = [
            [sg.Input(key="input"), sg.Button("Edit"),sg.Button("Delete"),sg.Button("Back")],
            [GuiLayouts.list_box],
            [sg.Text("Herb List",key="text", font=("Calibri",14), justification="center")]
        ]
        GuiLayouts.window = sg.Window("Edit Herb", layout, finalize=True)

        while True:
            event, values = GuiLayouts.window.read()
            if event == sg.WIN_CLOSED:
                break