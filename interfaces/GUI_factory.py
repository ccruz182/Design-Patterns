import abc

class GUIFactory(abc.ABC):
    @abc.abstractmethod
    def create_button():
        pass

    @abc.abstractmethod
    def create_checkbox():
        pass