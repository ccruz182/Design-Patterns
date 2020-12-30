import abc

class Vehicle(abc.ABC):
    @abc.abstractmethod
    def get_type(self):
        pass

    @abc.abstractmethod
    def get_location(self):
        pass

    @abc.abstractmethod
    def set_location(self, location: tuple):
        pass