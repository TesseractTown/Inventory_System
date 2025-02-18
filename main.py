#Inventory System that allows you to track items you have in your inteventory and add and subtract them.
#Possible Later system to see what items you can craft based on your items in your inventory


class HerbManager:
    def __init__(self):
        self.herb_dictionary = {}

    def create_herbs(self):
        herb_name = input("Enter the Herb's Name: ")
        how_many_herbs = int(input("How Many Herbs of This Type do You Have?: "))

        self.herb_dictionary[herb_name] = how_many_herbs

    def add_herbs(self):
        edit_herb_name = input("What Herb Are You Adding To?")
        edit_herb_total = int(input("How Many Are You Adding?"))
       
        
def main():
    current_herb = HerbManager()
    current_herb.create_herbs()
    print(current_herb.herb_dictionary.items)

if __name__ == "__main__":
    main()