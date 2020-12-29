class AutomaticCar():
    def __init__(self, seats, transmission):
        self.seats = seats
        self.transmission = transmission
        self._type = "AUTOMATIC"

    def get_specifications(self):
        return "TYPE={}, # seats={}, Transmission={}".format(self._type, self.seats, self.transmission)
        