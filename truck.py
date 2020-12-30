from interfaces.vehicle import Vehicle

class Truck(Vehicle):
    def get_type(self):
        return "Truck"

    def set_location(self, location):
        self.location = location
    
    def get_location(self):
        return self.location