from interfaces.city import City
from cities.asian_city import AsianCity

class AsianCityAdapter(City):
    def __init__(self, asian_city: AsianCity):
        self.asian_city = asian_city

    def get_name(self):
        return self.asian_city.name

    def get_temperature(self):
        return (self.asian_city.temperature * 1.8) + 32

    def get_temperature_scale(self):
        return 'Fahrenheit'

    def get_has_weather_warning(self):
        return self.asian_city.has_weather_warning

    def set_has_weather_warning(self, has_weather_warning: bool):
        self.asian_city.has_weather_warning = has_weather_warning