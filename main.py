import kivy
kivy.require('2.3.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
     def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs) #o que significa ess código
        self.col = 3
        self.rows = 3

class MyCustomButton(Widget):
    pass

class TrackingApp(App):
    def build(self):
        self.submit = Button(text="O Ônibus Chegou", font_size=40) 
        # self.add_widget(self.submit)
        self.title = 'Tracking Bus App'
        return self.submit
        

if __name__ == '__main__':
    TrackingApp().run()
