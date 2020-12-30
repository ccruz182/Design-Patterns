from interfaces.button import Button
from interfaces.size_button import SizeButton

class DropdownButton(Button):
    def __init__(self, size_button: SizeButton):
        self.size_button = size_button

    def draw(self):
        self.size_button.set_size()
        print("Drawing a DropdownButton")