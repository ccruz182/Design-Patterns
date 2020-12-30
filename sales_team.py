from interfaces.payee import Payee

class SalesTeam(Payee):
    def __init__(self):
        self.payees = []

    def add_payee(self, payee: Payee):
        self.payees.append(payee)

    def pay_expenses(self, amount: int):
        [p.pay_expenses(amount) for p in self.payees]