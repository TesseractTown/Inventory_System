import PySimpleGUI as sg
import HerbManager
import main

herbManager = HerbManager.HerbManager()

class GuiLayouts:
    def home_page_layout():


        GuiLayouts.herb_names = [
            herbManager.get_dict_keys()
        ]

        GuiLayouts.list_box = sg.Listbox(GuiLayouts.herb_names,
                                         size= (20,4),
                                         font=("Calibri", 14),
                                         expand_y=True,
                                         enable_events=True,
                                         key="list")


        GuiLayouts.herb_values = [
            herbManager.get_dict_values()
        ]

        GuiLayouts.list_box_values = sg.Listbox(GuiLayouts.herb_values,
                                         size= (20,4),
                                         font=("Calibri", 14),
                                         expand_y=True,
                                         enable_events=True)
        
        layout = [
            [sg.Text("Herb Inventory")],
            [sg.Button("Herb Create"), sg.Button("Delete")],
            [GuiLayouts.list_box, GuiLayouts.list_box_values],
            [sg.Button("Add"), sg.Button("Subtract")],
        ]

        GuiLayouts.window = sg.Window("Herb Inventory", layout, finalize=True)

        while True:
            event, values = GuiLayouts.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Herb Create":
       
                herbManager.create_herbs()
                GuiLayouts.window[GuiLayouts.home_page_layout()].refresh()

            elif event == "Add":
                herbManager.add_herbs()

            elif event == "Delete":
                print("Delete")

            elif event == "Subtract":
                print("Subtract")