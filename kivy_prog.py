import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)
        self.add_widget(Label(text="Remarks: "))
        self.remarks = TextInput(multiline=False)
        self.add_widget(self.remarks)

class MyLabelApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyLabelApp().run()


