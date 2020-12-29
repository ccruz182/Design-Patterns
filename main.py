from interfaces.price_calculator import PriceCalculator
from calculators.car_calculator import CarCalculator
from calculators.truck_calculator import TruckCalculator

from foreign_calculators.uk_car_calculator import UKCarCalculator
from adapters.car_calculator_adapter import CarCalculatorAdapter

def print_vehicle_price(calculator: PriceCalculator):
    print("Price of the vechicle: {}".format(calculator.calculate_price()))



car_price_calculator = CarCalculator("Mazda", 5)
print_vehicle_price(car_price_calculator)

truck_price_calculator = TruckCalculator(10, 2000)
print_vehicle_price(truck_price_calculator)

# Adapter
uk_car_calculator = UKCarCalculator(5, 13)
adapter = CarCalculatorAdapter(uk_car_calculator)
print_vehicle_price(adapter)