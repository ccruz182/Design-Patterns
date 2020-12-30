from vehicle_factory import VehicleFactory


factory = VehicleFactory()

v1 = factory.get_vehicle("0")
v2 = factory.get_vehicle("0")

print(v1, v2)