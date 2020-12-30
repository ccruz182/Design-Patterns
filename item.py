class Item():
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return "name={},price={},quantity={}".format(self.name, self.price, self.quantity)
