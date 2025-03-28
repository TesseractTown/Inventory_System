
# import HerbManager

# herbManager = HerbManager.HerbManager()

class HerbRecipes:
    def __init__(self):
        self.herb_recipe_dict = {}

    def create_herb_recipe(self):
        self.herb_recipe_dict = {}

        recipe_name = ("What is the Name of Your Recipe?")
    
        new_herb = ("Would you like to add a new ingredient? Y/N")

        new_recipe = []

        while new_herb == "Y":
            herb_name = ("Please Enter a Herb Name:",)
            herb_qty =("Please enter a herb quanity")
            print(f"You have added {herb_qty} {herb_name} to the recipe {recipe_name}")
            new_recipe.append({herb_name: herb_qty})
            new_herb = ("Would you like to add a new ingredient? Y/N")

            print("Adding new recipe to recipe book.....")
            self.herb_recipe_dict[recipe_name] = new_recipe
            print(self.herb_recipe_dict)
    
    def delete_herb_recipe(self):
      edit_recipe_name = ("What Recipe Do You Want to Delete?")
      del self.herb_recipe_dict[edit_recipe_name]

    def get_dict_keys_recipe(self):
        print(self.herb_recipe_dict)
        recipe_list = []
        for key, value in self.herb_recipe_dict.items():
            recipe_list.append((key,value))

        return recipe_list

