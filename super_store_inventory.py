from interfaces.inventory import Inventory

from item import Item

class SuperStoreInventory(Inventory):
    def __init__(self):
        self.inventory = [
            Item("P1", 19.0, 3),
            Item("P2", 300, 4)
        ]
    
    def get_inventory(self):
        return self.inventory