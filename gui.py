from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
import HerbManager
import main
import HerbRecipies

herbManagerobj = HerbManager.HerbManager()
herbRecipies = HerbRecipies.HerbRecipes()

#CREATE HERB LAYOUT

createHerbLayout = GridLayout()
createHerbLayout.cols = 1
createHerbLayout.add_widget(Label(text=("What is the name of the Herb?")))
createHerbLayout.add_widget(herbName = TextInput(multiline= False,
                    padding_y= (20,20),
                    size_hint= (0.5, 0.5)))

createHerbLayout.add_widget(Label(text=("How Many of this Herb Do you Have?")))
createHerbLayout.add_widget(how_many_herbs = TextInput(multiline= False,
                    padding_y= (20,20),
                    size_hint= (0.5, 0.5)))
createHerbLayout.add_widget(done_button = Button(

            text = "Done",
            size_hint= (0.2,0.1),
            bold= True,
            background_color ='#00FFCE',
)
)
createHerbLayout.done_button.bind(on_press=herbManagerobj.create_herbs())


#DELETE HERB LAYOUT

deleteHerbLayout= GridLayout()
deleteHerbLayout.cols =1 
deleteHerbLayout.add_widget(Label(text=("What is the name of the Herb you would like to delete?")))
deleteHerbLayout.add_widget(TextInput(multiline= False,
                    padding_y= (20,20),
                    size_hint= (0.5, 0.5)))
deleteHerbLayout.add_widget(Button(

            text = "Done",
            size_hint= (0.2,0.1),
            bold= True,
            background_color ='#00FFCE',
))
createHerbPopup= Popup(
title="Create Herb",
content=createHerbLayout
)

deleteHerbPopup=Popup(
    title="Delete Herb",
    content=deleteHerbLayout
)

class GuiLayouts(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        self.topLabel = Label(
            text="Herb Manager",
            font_size=18
            )
        self.window.add_widget(self.topLabel)

        #Buttons

        self.AddHerb = Button(
            text = "Add Herb",
            size_hint= (0.2,0.1),
            bold= True,
            background_color ='#00FFCE',
        )
        self.AddHerb.bind(on_press=createHerbPopup.open)
        self.window.add_widget(self.AddHerb)


        self.deleteHerb = Button(
            text = "Delete Herb",
            size_hint= (0.2,0.1),
            bold= True,
            background_color ='#00FFCE',
        )
        self.deleteHerb.bind(on_press=deleteHerbPopup.open)
        self.window.add_widget(self.deleteHerb)


        self.editHerbAmount = Button(
            text = "Edit Herb",
            size_hint= (0.2,0.1),
            bold= True,
            background_color ='#00FFCE',
        )
        #self.AddHerb.bind(on_press=herbManager.remove_herb_amount())
        self.window.add_widget(self.editHerbAmount)

        self.window.add_widget(
            Image(source="Divider.gif"))


        self.createHerbRecipe = Button(
            text = "Create Herb Recipe",
            size_hint= (0.2,0.1),
            bold= True,
            background_color ='#00FFCE',
        )
        #self.AddHerb.bind(on_press=herbManager.remove_herb_amount())
        self.window.add_widget(self.createHerbRecipe)

        self.deleteHerbRecipe = Button(
            text = "Delete Recipe",
            size_hint= (0.2,0.1),
            bold= True,
            background_color ='#00FFCE',
        )
        #self.AddHerb.bind(on_press=herbManager.remove_herb_amount())
        self.window.add_widget(self.deleteHerbRecipe)



        return self.window

    
GuiLayouts().run()