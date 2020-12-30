from interfaces.inventory import Inventory

class Store():
    def __init__(self, name: str, location: str, inventory: Inventory):
        self.name = name
        self.location = location
        self.inventory = inventory
    
    def print_name(self):
        print("Name={}".format(self.name))
    
    def print_location(self):
        print("Location={}".format(self.location))
    
    def print_inventory(self):
        print("Inventory={}".format(self.inventory.get_inventory()))