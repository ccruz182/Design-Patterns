class UKCarCalculator():
    def __init__(self, age: int, damage: int):
        self.age = age
        self.damage = damage
        self.average_price = 9500

    def get_price(self) -> int:
        return int((self.average_price - (225 * self.age)) - (80 * self.damage))