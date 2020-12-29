from weather_warning import WeatherWarning
from cities.north_american_city import NorthAmericanCity
from cities.asian_city import AsianCity
from adapters.asian_city_adapter import AsianCityAdapter

weather_warning = WeatherWarning()

chicago = NorthAmericanCity('Chicago', 16)
weather_warning.post_warning(chicago)

portland = NorthAmericanCity('Portland', 70)
weather_warning.post_warning(portland)

bangkok = AsianCity('Bangkok', 50)
adapter = AsianCityAdapter(bangkok)
weather_warning.post_warning(adapter)