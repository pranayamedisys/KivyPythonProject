# Program to Show how to create textinput
# with button in kivy using .kv file

##################################################
# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.1')

# Widgets are elements
# of a graphical user interface
# that form part of the User Experience.
from kivy.uix.widget import Widget

# The TextInput widget provides a
# box for editable plain text
from kivy.uix.textinput import TextInput

# BoxLayout arranges widgets in either
# in a vertical fashion that is
# one on top of another or in a horizontal
# fashion that is one after another.
from kivy.uix.boxlayout import BoxLayout

# to change the kivy default settings we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)


# class in which we are creating the Textinput and btn
# in .kv file to be named main.kv
class MainApp(App):
    def on_text(instance, value):
        print('The widget', instance, 'have:', value)
        textinput = TextInput()
        textinput.bind(text=instance.on_text)

if __name__ == '__main__':
    MainApp().run()

