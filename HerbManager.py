import PySimpleGUI as sg

class HerbManager:
    def __init__(self):
        self.herb_dictionary = {}

    def create_herbs(self):
        #herb_name = input("Enter the Herb's Name: ")
        #how_many_herbs = int(input("How Many Herbs of This Type do You Have?: "))

        
        herb_name = sg.popup_get_text("Enter What Herb You Want to Create: ", title= "Textbox")
        how_many_herbs = sg.popup_get_text("Enter How Many of That Herb You Have: ", title="Textbox")

        self.herb_dictionary[herb_name] = how_many_herbs
        
        print(self.herb_dictionary.items)

    def add_herbs(self):
        edit_herb_name = input("What Herb Are You Adding To?")