class Watercraft(Vehicle):
    def __init__(self, id: int, manuf, name, color, date_of_manufacturing, state, fuel: Vehicle_fuel):
        super().__init__(id, manuf, name, color, date_of_manufacturing, state, fuel)