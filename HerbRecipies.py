import PySimpleGUI as sg
import HerbManager
import gui

herbManager = HerbManager.HerbManager()

class HerbRecipes:
    def __init__(self):
        self.herb_recipe_dict = {}

    def create_herb_recipe(self):
        self.herb_recipe_dict = {}

        recipe_name = sg.popup_get_text("What is the Name of Your Recipe?", title="Textbox")
    
        new_herb = sg.popup_get_text("Would you like to add a new ingredient? Y/N")

        new_recipe = []

        while new_herb == "Y":
            herb_name = sg.popup_get_text("Please Enter a Herb Name:", title="Textbox")
            herb_qty = sg.popup_get_text("Please enter a herb quanity",title="Textbox")
            print(f"You have added {herb_qty} {herb_name} to the recipe {recipe_name}")
            new_recipe.append({herb_name: herb_qty})
            new_herb = sg.popup_get_text("Would you like to add a new ingredient? Y/N")

            print("Adding new recipe to recipe book.....")
            self.herb_recipe_dict[recipe_name] = new_recipe
            print(self.herb_recipe_dict)
    
    def delete_herb_recipe(self):
      edit_recipe_name = sg.popup_get_text("What Recipe Do You Want to Delete?", title="Textbox")
      del self.herb_recipe_dict[edit_recipe_name]

    def get_dict_keys_recipe(self):
        print(self.herb_recipe_dict)
        recipe_list = []
        for key, value in self.herb_recipe_dict.items():
            recipe_list.append((key,value))

        return recipe_list

