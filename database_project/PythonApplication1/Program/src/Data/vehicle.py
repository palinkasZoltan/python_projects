from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    car_states = ['New', 'Used', 'Renovated', 'Broken']

    def __init__(self, id:int, manuf, name, color, date_of_manufacturing, state, fuel:Vehicle_fuel):
        self.id = id
        self.name = name
        self.color = color
        self.date_of_manufacturing = date_of_manufacturing
        self.state = state
        self.manuf = manuf
        self.fuel = fuel

    @abstractmethod
    def set_state(self, new_state):
        if new_state in self.car_states:
            self.state = new_state
            return True
        return False

    def __str__(self) -> str:
        return f'Vehicle manufacturer:\t{self.manuf}\nVehicle name:\t{self.name}\nColor:\n{self.color}'



