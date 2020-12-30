from interfaces.vehicle import Vehicle

class Car(Vehicle):
    def get_type(self):
        return "Car"

    def set_location(self, location):
        self.location = location
    
    def get_location(self):
        return self.location