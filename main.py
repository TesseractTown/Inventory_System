#Inventory System that allows you to track items you have in your inteventory and add and subtract them.
#Possible Later system to see what items you can craft based on your items in your inventory
import HerbManager
import gui
 
def main():
    import sysconfig; print(sysconfig.get_path("scripts"))
    import site; print(site.USER_BASE + "\\Scripts")
    #gui.GuiLayouts.home_page_layout()
    gui.GuiLayouts().run()
    #current_herb = HerbManager()
    #print(current_herb.herb_dictionary.items)
    

if __name__ == "__main__":
    main()