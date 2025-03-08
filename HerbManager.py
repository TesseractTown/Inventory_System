import PySimpleGUI as sg

class HerbManager:
    def __init__(self):
        self.herb_dictionary = {}

    def create_herbs(self):
        
        herb_name = sg.popup_get_text("Enter What Herb You Want to Create: ", title= "Textbox")
        how_many_herbs = int(sg.popup_get_text("Enter How Many of That Herb You Have: ", title="Textbox"))

        self.herb_dictionary[herb_name] = how_many_herbs

       # for key, value in dict.items(self.herb_dictionary):
          #  print(key, value)

    def add_herbs(self):
      edit_herb_name = sg.popup_get_text("What Herb Do You Want to Change?", title="Textbox")
      edit_herb_value = int(sg.popup_get_text("How Many To Add?", title="Textbox"))
      self.herb_dictionary[edit_herb_name] += edit_herb_value

    def remove_herb_amount(self):
     
      edit_herb_name = sg.popup_get_text("What Herb Do You Want to Change?", title="Textbox")
      edit_herb_value = int(sg.popup_get_text("How Many To Subtract?", title="Textbox"))
      self.herb_dictionary[edit_herb_name] -= edit_herb_value
      if self.herb_dictionary[edit_herb_name] <= 0:
          self.herb_dictionary[edit_herb_name] = 0

    def delete_herb(self):
        
      edit_herb_name = sg.popup_get_text("What Herb Do You Want to Delete?", title="Textbox")
      del self.herb_dictionary[edit_herb_name]
      

    def get_dict_keys(self):
        print(self.herb_dictionary)
        herb_list = []
        for key, value in self.herb_dictionary.items():
            herb_list.append((key,value))

        return herb_list