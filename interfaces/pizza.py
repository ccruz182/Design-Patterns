import abc

class Pizza(abc.ABC):
    @abc.abstractmethod
    def get_toppings(self):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass