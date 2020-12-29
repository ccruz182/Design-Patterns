from interfaces.price_calculator import PriceCalculator


class CarCalculator(PriceCalculator):

    def __init__(self, model: str, age: int):
        self.model = model
        self.age = age

    def get_retail_price(self):
        if self.model == "Ford":
            return 3000
        elif self.model == "Mazda":
            return 3500
        elif self.model == "BMW":
            return 4000
        else:
            return 2500

    def calculate_price(self) -> str:
        return "{}\tUSD".format(int(self.get_retail_price() - (250 * self.age)))
