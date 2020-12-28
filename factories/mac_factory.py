from interfaces.GUI_factory import GUIFactory
from buttons.mac_button import MacOSButton
from checkbox.mac_checkbox import MacOSCheckbox

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()
    
    def create_checkbox(self):
        return MacOSCheckbox()