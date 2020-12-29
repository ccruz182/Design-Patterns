class ManualCar():
    def __init__(self, seats, transmission):
        self.seats = seats
        self.transmission = transmission
        self._type = "MANUAL"

    def get_specifications(self):
        return "TYPE={}, # seats={}, Transmission={}".format(self._type, self.seats, self.transmission)
        