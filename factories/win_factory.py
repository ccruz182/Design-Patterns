from interfaces.GUI_factory import GUIFactory
from buttons.win_button import WindowsButton
from checkbox.win_checkbox import WindowsCheckbox

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()