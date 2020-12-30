import abc

class Book(abc.ABC):
    @abc.abstractmethod
    def checkout(self):
        pass

    @abc.abstractmethod
    def return_book(self):
        pass