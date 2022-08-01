from sqlite3 import Date

class Manufacturer():

    def __init__(self, id: int, name, founded: Date, HQ_location, nr_of_locations, nr_of_employees):
        self.id = id
        self.name = name
        self.founded = founded
        self.HQ_location = HQ_location
        self.nr_of_locations = nr_of_locations
        self.nr_of_employees = nr_of_employees