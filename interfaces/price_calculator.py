import abc

class PriceCalculator(abc.ABC):
    @abc.abstractmethod
    def calculate_price(self):
        pass