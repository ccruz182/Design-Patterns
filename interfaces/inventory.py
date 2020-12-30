import abc

from item import Item

class Inventory(abc.ABC):
    @abc.abstractmethod
    def get_inventory(self):
        pass