import PySimpleGUI as sg

class HerbManager:
    def __init__(self):
        self.herb_dictionary = {}

    def create_herbs(self):
        
        herb_name = sg.popup_get_text("Enter What Herb You Want to Create: ", title= "Textbox")
        how_many_herbs = sg.popup_get_text("Enter How Many of That Herb You Have: ", title="Textbox")

        self.herb_dictionary[herb_name] = how_many_herbs

        for key, value in dict.items(self.herb_dictionary):
            print(key, value)
        
 

    def add_herbs(self):
        edit_herb_name = sg.popup_get_text("What Herb Do You Want to Change?", title="Textbox")

    def remove_herb_amount(self):
        edit_herb_name = input("yada")

    def get_dict_keys(self):
        for key, value in dict.items(self.herb_dictionary):
                      herb_list = key

        print(herb_list)