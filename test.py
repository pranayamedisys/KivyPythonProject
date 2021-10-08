from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivy.uix.label import Label
class KivyProj(MDApp):

    def build(self):
        screen =Screen()

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
                               'center_y': 0.5})
        screen.add_widget(btn)
        return screen
KivyProj().run()
