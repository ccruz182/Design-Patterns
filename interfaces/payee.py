import abc

class Payee(abc.ABC):
    @abc.abstractmethod
    def pay_expenses(self, amount: int):
        pass