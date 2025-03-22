import gui

Guiobj = gui

class HerbManager:
    def __init__(self):
        self.herb_dictionary = {}

    def create_herbs(self):

        self.herb_dictionary[Guiobj.herb_name] = Guiobj.how_many_herbs



    def add_herbs(self):
      edit_herb_name = ("What Herb Do You Want to Change?")
      edit_herb_value = int(("How Many To Add?"))
      self.herb_dictionary[edit_herb_name] += edit_herb_value

    def remove_herb_amount(self):
     
      edit_herb_name = ("What Herb Do You Want to Change?")
      edit_herb_value = int(("How Many To Subtract?"))
      self.herb_dictionary[edit_herb_name] -= edit_herb_value
      if self.herb_dictionary[edit_herb_name] <= 0:
          self.herb_dictionary[edit_herb_name] = 0

    def delete_herb(self):
        
      edit_herb_name = ("What Herb Do You Want to Delete?")
      del self.herb_dictionary[edit_herb_name]
      

    def get_dict_keys(self):
        print(self.herb_dictionary)
        herb_list = []
        for key, value in self.herb_dictionary.items():
            herb_list.append((key,value))

        return herb_list