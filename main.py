#Inventory System that allows you to track items you have in your inteventory and add and subtract them.
#Possible Later system to see what items you can craft based on your items in your inventory
import HerbManager
 
def main():
    current_herb = HerbManager()
    current_herb.create_herbs()
    print(current_herb.herb_dictionary.items)

if __name__ == "__main__":
    main()