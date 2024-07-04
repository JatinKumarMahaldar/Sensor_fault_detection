from sensor.configuration.mongo_db_connections import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys




def try_exception():
    try:
        logging.info("we are dividing 1 by zero")
        
        a = 1 / 0
        
    except Exception as error:
        raise SensorException(error , sys)
    
if __name__ == '__main__':
    try:
        try_exception()
    except Exception as error:
        raise SensorException(error , sys)
    
    
    
    
    
    
"""
    mongo_db_client = MongoDBClient()
    print(mongo_db_client.client)
    print(mongo_db_client.database)
    print(mongo_db_client.database_name)""" 