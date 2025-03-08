import PySimpleGUI as sg
import HerbManager
import main
import HerbRecipies

herbManager = HerbManager.HerbManager()
herbRecipies = HerbRecipies.HerbRecipes()

class GuiLayouts:
    def home_page_layout():


        GuiLayouts.herb_names = herbManager.get_dict_keys()
        GuiLayouts.recipe_names = herbRecipies.get_dict_keys_recipe()
        

        GuiLayouts.list_box = sg.Listbox(GuiLayouts.herb_names,
                                         size= (20,4),
                                         font=("Calibri", 14),
                                         expand_y=True,
                                         enable_events=True,
                                         key="list")


        GuiLayouts.list_box_recipes = sg.Listbox(GuiLayouts.recipe_names,
                                         size= (20,4),
                                         font=("Calibri", 14),
                                         expand_y=True,
                                         enable_events=True,
                                        )
        
        layout = [
            [sg.Text("Herb Inventory")],
            [sg.Button("Herb Create"), sg.Button("Delete")],
            [GuiLayouts.list_box, GuiLayouts.list_box_recipes],
            [sg.Button("Add"), sg.Button("Subtract"), sg.Button("Create Recipe")],
        ]

        GuiLayouts.window = sg.Window("Herb Inventory", layout, finalize=True)

        while True:
            event, values = GuiLayouts.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Herb Create":
       
                herbManager.create_herbs()
                GuiLayouts.window[GuiLayouts.home_page_layout()].update()

            elif event == "Add":
                herbManager.add_herbs()
                GuiLayouts.window[GuiLayouts.home_page_layout()].refresh()
                

            elif event == "Delete":
                herbManager.delete_herb()
                GuiLayouts.window[GuiLayouts.home_page_layout()].refresh()

            elif event == "Subtract":
                herbManager.remove_herb_amount()
                GuiLayouts.window[GuiLayouts.home_page_layout()].refresh()
            elif event == "Create Recipe":
                herbRecipies.create_herb_recipe()
                GuiLayouts.window[GuiLayouts.home_page_layout()].refresh()
                print (herbRecipies.get_dict_keys_recipe())