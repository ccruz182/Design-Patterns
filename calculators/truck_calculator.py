from interfaces.price_calculator import PriceCalculator


class TruckCalculator(PriceCalculator):

    def __init__(self, age: int, miles: int):
        self.age = age
        self.miles = miles
        self.average_price = 10000


    def calculate_price(self) -> str:
        return "{}\tUSD".format(int((self.average_price - (250 * self.age)) - (0.25 * self.miles)))
