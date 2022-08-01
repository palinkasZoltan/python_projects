from aircraft import Aircraft
from DataEnums.vehicleFuel import Vehicle_fuel

class Drone(Aircraft):

    def __init__(self, id: int, manuf, name, color, date_of_manufacturing, state, fuel: Vehicle_fuel):
        super().__init__(id, manuf, name, color, date_of_manufacturing, state, fuel)