from interfaces.price_calculator import PriceCalculator
from foreign_calculators.uk_car_calculator import UKCarCalculator

class CarCalculatorAdapter(PriceCalculator):
    def __init__(self, uk_car_calculator: UKCarCalculator):
        self.uk_car_calculator = uk_car_calculator

    def calculate_price(self) -> str:
        return "{}\tGBP".format(self.uk_car_calculator.get_price())