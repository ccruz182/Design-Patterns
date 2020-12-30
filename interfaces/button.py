import abc

class Button(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass