from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import HerbManager
import main
import HerbRecipies

herbManager = HerbManager.HerbManager()
herbRecipies = HerbRecipies.HerbRecipes()

class GuiLayouts(App):
    def home_page_layout(self):
       layout = BoxLayout(orientation='vertical')
       b1 = Button(text='button 1')
       b2 = Button(text='button 2')

       layout.add_widget(b1)
       layout.add_widget(b2)

       return layout

    
GuiLayouts().run()