from landcraft import Landcrafts
from DataEnums.vehicleFuel import Vehicle_fuel
from DataEnums.motorcycleTypes import Motorcycle_types

class Motorcycle(Landcrafts):

    def __init__(self, id: int, manuf, name, color, date_of_manufacturing, state, fuel: Vehicle_fuel, type: Motorcycle_types):
        super().__init__(id, manuf, name, color, date_of_manufacturing, state, fuel, 2)
        self.type = type