

class HerbManager:
    def __init__(self):
        self.herb_dictionary = {}

    def create_herbs(self):
        herb_name = input("Enter the Herb's Name: ")
        how_many_herbs = int(input("How Many Herbs of This Type do You Have?: "))

        self.herb_dictionary[herb_name] = how_many_herbs

    def add_herbs(self):
        edit_herb_name = input("What Herb Are You Adding To?")