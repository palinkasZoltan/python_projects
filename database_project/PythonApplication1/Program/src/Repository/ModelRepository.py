import sqlalchemy as sal
import pandas as pd
from ..data_connection import Data_context

class VehicleRepository(Data_context):
    
    def add_car_model(self):
        query = sal.insert(self.carModelTypes).values(id=8, model='test')

        self.connection.execute(query)