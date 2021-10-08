
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

kv = '''
<ColoredLabel>:
    size: (100,100)

    background_color:
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
    '''

Builder.load_string(kv)

class ColoredLabel(Label):
    background_color = ListProperty((0,0,0,1))

class MyApp(App):
    def build(self):
        f = FloatLayout()
        layout = BoxLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

        '''label1 = ColoredLabel(text="jenkins", background_color=(160,160,160,.5))
        layout.add_widget(label1)

        label2 = ColoredLabel(text="git", background_color=(160,160,160,.5))
        layout.add_widget(label2)

        label3 = ColoredLabel(text="portal", background_color=(160,160,160,.5))
        layout.add_widget(label3)

        f.add_widget(layout)


        return f'''

if __name__ == "__main__":
    MyApp().run()
