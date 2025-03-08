import PySimpleGUI as sg
import HerbManager
import gui

herbManager = HerbManager.HerbManager()

class HerbRecipes:
    def __init__(self):
        self.herb_recipe_dict = {}

    def create_herb_recipe(self):
        herb_recipe_dict = {}

        recipe_name = sg.popup_get_text("What is the Name of this Recipe?", title="Textbox")
        herb_name_1 = sg.popup_get_text("What Herb?", title="Textbox")
        yes_or_no = sg.popup_get_text("Add Another Herb? Y/N", title="Textbox")
        if yes_or_no == "Y":
            herb_name_2 = sg.popup_get_text("What Herb?")
            yes_or_no = sg.popup_get_text("Add Another Herb?", title="Textbox")
        else:
            return
        if yes_or_no == "Y":
            herb_name_3 = sg.popup_get_text("What Herb?")
        print (herb_recipe_dict)

        herb_recipe_dict[recipe_name] = herb_name_1, herb_name_2, herb_name_3 
    
    
    def delete_herb_recipe():
        pass


    def get_dict_keys_recipe(self):
        print(self.herb_recipe_dict)
        recipe_list = []
        for key, value in self.herb_recipe_dict.items():
            recipe_list.append((key,value))

        return recipe_list

