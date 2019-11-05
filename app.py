import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class ButtonApp(App):

    def build(self):
        return Button()

    def on_press_button(self, instance):
        print("You pressed the button")

if __name__ == "__main__":
    app = ButtonApp()
    app.run()