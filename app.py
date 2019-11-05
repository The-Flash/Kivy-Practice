import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class MainApp(App):

    def build(self):
        button = Button(text="Hello from Kivy",
                    size_hint=(.5, .5),
                    pos_hint={"center_x": .5, "center_y": .5}
        )
        button.bind(on_press=self.on_press_button)
        return button

    def on_press_button(self, instance):
        print("You pressed the button")

if __name__ == "__main__":
    app = MainApp()
    app.run()