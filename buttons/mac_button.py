from interfaces.button import Button


class MacOSButton(Button):
    def paint(self):
        print("Painting a MacOS Button")