from interfaces.builder import Builder

class Director():
    def __init__(self, builder: Builder):
        self.builder = builder
    
    def build_city_car(self, _type):
        if _type == "automatic":
            self.builder.set_seats(4)
            self.builder.set_transmission("automatic-v1")
        elif _type == "manual":
            self.builder.set_seats(4)
            self.builder.set_transmission("manual-v1")
        else:
            raise ValueError("type is not correct")

    def build_race_car_premium(self):
        self.builder.set_seats(2)
        self.builder.set_transmission('automatic-v2')

    def build_race_car(self):
        self.builder.set_seats(2)
        self.builder.set_transmission('manual-v2')