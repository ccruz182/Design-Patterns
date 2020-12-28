import abc

class Button(abc.ABC):
    @abc.abstractmethod
    def paint(self):
        pass