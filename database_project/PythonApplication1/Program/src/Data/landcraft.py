from abc import ABC
from vehicle import Vehicle
from DataEnums.vehicleFuel import Vehicle_fuel

class Landcrafts(Vehicle, ABC):
    
    def __init__(
        self,
        id: int,
        manuf,
        name,
        color,
        date_of_manufacturing,
        state,
        fuel: Vehicle_fuel,
        nr_of_wheels: int
        ):
        super().__init__(id, manuf, name, color, date_of_manufacturing, state, fuel)
        self.nr_of_wheels = nr_of_wheels