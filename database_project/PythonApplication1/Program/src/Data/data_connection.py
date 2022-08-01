from sqlalchemy import Table, MetaData
import sqlalchemy as sal
import pandas as pd
import urllib

class Data_context():

    def __init__(self):        
        params = urllib.parse.quote_plus('Driver={SQL Server};Server=EVH11858NB;Database=Python_test;Trusted_Connection=True;')

        engine = sal.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(params))
        self.connection = engine.connect()
        metadata = MetaData()

        self.carModelTypes: Table = sal.Table('Car_Model_Types', metadata, autoload=True, autoload_with=engine)
        self.manufacturers: Table = sal.Table('Vehicle_Manufacturers', metadata, autoload=True, autoload_with=engine)

        #query = sal.select([self.carModelTypes])
        #Result_proxy = self.connection.execute(query)
        #Result_set = Result_proxy.fetchall()

        #sql_query = sal.select([self.carModelTypes])
        #data = pd.read_sql(sql_query, self.connection)
        #sorted_values = data.sort_values('id')
        #print(self.GetManufacturerBy(1))
        
    @property
    def get_connection(self):
        return self.connection

    def GetAllCarModels(self):
        sql_query = 'SELECT * FROM Car_Model_Types'
        data = pd.read_sql(sql_query, self.connection)
        sorted_values = data.sort_values('id')
        print(sorted_values) 

    def GetOneCarModel(self, id: int):
        sql_query = f'SELECT * FROM Car_Model_Types WHERE Car_Model_Types.id={id}'

        data = pd.read_sql(sql_query, self.connection)
        print(data.values)

    def GetManufacturerBy(self, id: int):
        sql_query = sal.select([self.manufacturers]).where(self.manufacturers.columns.manufID == id)

        data = pd.read_sql(sql_query, self.connection)
        return data.values