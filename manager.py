from interfaces.payee import Payee

class Manager(Payee):
    def __init__(self, name):
        self.name = name

    def pay_expenses(self, amount: int):
        print("{} has been paid ${}".format(self.name, amount))