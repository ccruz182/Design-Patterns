import abc

class Builder(abc.ABC):
    @abc.abstractmethod
    def set_car_type(self, _type: str):
        pass

    @abc.abstractmethod
    def set_seats(self, seats: int):
        pass

    @abc.abstractmethod
    def set_transmission(self, transmission: str):
        pass