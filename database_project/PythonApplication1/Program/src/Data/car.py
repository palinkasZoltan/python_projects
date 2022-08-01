from landcraft import Landcrafts
from DataEnums.vehicleFuel import Vehicle_fuel
from DataEnums.carTypes import Car_types
from DataEnums.carModelTypes import Car_model_types

class Car(Landcrafts):

    def __init__(self, id: int, manuf, name, color, date_of_manufacturing, state, fuel: Vehicle_fuel, type: Car_types, model: Car_model_types):
        super().__init__(id, manuf, name, color, date_of_manufacturing, state, fuel, 4)
        self.type = type
        self.model = model