from kivy.compat import unichr
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
KV = '''
MDScreen:

    MDBoxLayout:
        id: box
        orientation: "vertical"


        MDToolbar:
            halign: "center"
            title: "Medisys EduTech Private Limited"
            
        MDLabel:
            halign: "center"
    
'''

class KivyProj(MDApp):

    def build(self):
        screen = Builder.load_string(KV)

        Height =MDTextField(text="enter the Height",pos_hint={'center_x': 0.52 ,'center_y': 0.8}, size_hint=(0.5,1))
        screen.add_widget(Height)

        Width = MDTextField(text="enter the Width", pos_hint={'center_x': 0.52, 'center_y': 0.7}, size_hint=(0.5, 1))
        screen.add_widget(Width)

        Dpi = MDTextField(text="enter the Dpi", pos_hint={'center_x': 0.52, 'center_y': 0.6}, size_hint=(0.5, 1))
        screen.add_widget(Dpi)

        Path = MDTextField(text="enter the Path", pos_hint={'center_x': 0.52, 'center_y': 0.5}, size_hint=(0.5, 1))
        screen.add_widget(Path)

        btn = Button(text="Submit !",
                     font_size="10sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(10, 0),
                     size_hint=(.1, .1),
                     pos_hint={'center_x': 0.52,
                               'center_y': 0.4})
        screen.add_widget(btn)
        return screen



KivyProj().run()
#by pranaya