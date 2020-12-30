import abc

class SizeButton(abc.ABC):
    @abc.abstractmethod
    def set_size(self):
        pass