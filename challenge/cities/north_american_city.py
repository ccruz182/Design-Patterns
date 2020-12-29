from interfaces.city import City

class NorthAmericanCity(City):
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature
        self.has_weather_warning = False

    def get_name(self):
        return self.name

    def get_temperature(self):
        return self.temperature

    def get_temperature_scale(self):
        return 'Fahrenheit'

    def get_has_weather_warning(self):
        return self.has_weather_warning

    def set_has_weather_warning(self, has_weather_warning: bool):
        self.has_weather_warning = has_weather_warning
