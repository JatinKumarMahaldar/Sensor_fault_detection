import sys
from typing import Optional

import numpy as np
import pandas as pd

from sensor.configuration.mongo_db_connections import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException


class SensorData():
    """this class helps in exporting entire mongo databse record as pandas dataframe"""
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise SensorException(e, sys)
        
    def export_collection_as_dataframe(self , colllection_name: str , database_name:Optional[str]= None):
        try:
            if database_name is None:
                collection = self.mongo_client.database(colllection_name)
            else:
                collection = self.mongo_client.client[database_name][colllection_name]
                
            df = pd.DataFrame(list(collection.find()))
            if "id" in df.columns:
                df.drop("id", axis=1, inplace=True)
            df.replace({"na", np.nan} , inplace=True)
            
            return df
        except Exception as e:
            raise SensorException(e, sys)