from interfaces.builder import Builder
from cars.automatic_car import AutomaticCar

class AutomaticCarBuilder(Builder):
    def set_car_type(self, _type: str):
        self._type = _type

    def set_seats(self, seats: int):
        self.seats = seats

    def set_transmission(self, transmission: str):
        self.transmission = transmission

    def get_car(self):
        return AutomaticCar(self.seats, self.transmission)