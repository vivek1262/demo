import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyLabelApp(App):
    def build(self):
        lbl = Label(text ="Label is Added on screen !!:):)")
        return lbl

if __name__ == "__main__":
    MyLabelApp().run()


