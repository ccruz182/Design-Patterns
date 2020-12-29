import abc

class City(abc.ABC):
    @abc.abstractmethod
    def get_name(self):
        pass
    
    @abc.abstractmethod
    def get_temperature(self):
        pass

    @abc.abstractmethod
    def get_temperature_scale(self):
        pass

    @abc.abstractmethod
    def get_has_weather_warning(self):
        pass

    @abc.abstractmethod
    def set_has_weather_warning(self, has_weather_warning: bool):
        pass
    