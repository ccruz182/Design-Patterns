from interfaces.inventory import Inventory
from super_store_inventory import SuperStoreInventory

class SuperStoreInventoryProxy(Inventory):
    def __init__(self):
        self.inventory: Inventory = None

    def get_inventory(self):
        if (self.inventory == None):
            self.inventory = SuperStoreInventory()
        

        return self.inventory.get_inventory()