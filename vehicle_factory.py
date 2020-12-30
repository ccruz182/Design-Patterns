from interfaces.vehicle import Vehicle

from car import Car
from truck import Truck

class VehicleFactory():
    def __init__(self):
        self.vehicles = {}

    def get_vehicle(self, _type):
        if _type in self.vehicles:
            return self.vehicles.get(_type)
        else:
            vehicle: Vehicle
            if (_type == "0"):
                vehicle = Car()
            else:
                vehicle = Truck
            
            self.vehicles[_type] = vehicle
            
            return vehicle



