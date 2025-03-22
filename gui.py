from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import HerbManager
import main
import HerbRecipies

herbManager = HerbManager.HerbManager()
herbRecipies = HerbRecipies.HerbRecipes()

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
        #self.AddHerb.bind(on_press=herbManager.create_herbs())
        self.window.add_widget(self.AddHerb)


        self.deleteHerb = Button(
            text = "Delete Herb",
            size_hint= (0.2,0.1),
            bold= True,
            background_color ='#00FFCE',
        )
        #self.AddHerb.bind(on_press=herbManager.delete_herb())
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