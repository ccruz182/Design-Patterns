from interfaces.payee import Payee

from manager import Manager
from salesperson import SalesPerson
from sales_team import SalesTeam


def pay(payee: Payee, amount: int):
    payee.pay_expenses(amount)

jane: Manager = Manager("Jane")
bob: SalesPerson = SalesPerson("Bob", jane)
sue: SalesPerson = SalesPerson("Sue", jane)

team: SalesTeam = SalesTeam()
team.add_payee(jane)
team.add_payee(bob)
team.add_payee(sue)

pay(jane, 100)
pay(bob, 110)
pay(sue, 120)

pay(team, 300)