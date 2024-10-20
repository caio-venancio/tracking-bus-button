import kivy
kivy.require('2.3.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MyCustomButton(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyCustomButton()


if __name__ == '__main__':
    MyApp().run()
