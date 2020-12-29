from director import Director
from builders.automatic_car_builder import AutomaticCarBuilder
from builders.manual_car_builder import ManualCarBuilder

acb = AutomaticCarBuilder()
at_director = Director(acb)

at_director.build_city_car('automatic')
print("CAR 1 specifications: {}".format(acb.get_car().get_specifications()))
at_director.build_race_car_premium()
print("CAR 2 specifications: {}".format(acb.get_car().get_specifications()))

mcb = ManualCarBuilder()
at_director = Director(mcb)
at_director.build_city_car('manual')
print("CAR 3 specifications: {}".format(mcb.get_car().get_specifications()))
