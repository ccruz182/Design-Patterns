from interfaces.city import City

class WeatherWarning():
    def __init__(self):
        self.max_temperature = 100
        self.min_temperature = 16

    def post_warning(self, city: City):
        label = ''
        if (city.get_temperature() >= self.max_temperature or city.get_temperature() <= self.min_temperature):
            label = 'WARNING! Current temperature in {} is {} {}'.format(city.get_name(), city.get_temperature(), city.get_temperature_scale())
            city.set_has_weather_warning(True)
        else:
            label = "Temperature in {} is OK".format(city.get_name())
        
        print(label)