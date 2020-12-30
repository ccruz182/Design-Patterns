from interfaces.payee import Payee

from manager import Manager

class SalesPerson(Payee):
    def __init__(self, name: str, manager: Manager):
        self.name = name
        self.manager = manager
    
    def pay_expenses(self, amount: int):
        print("{} has been paid ${}".format(self.name, amount))
