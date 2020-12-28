import abc

class Checkbox(abc.ABC):
    @abc.abstractmethod
    def paint(self):
        pass