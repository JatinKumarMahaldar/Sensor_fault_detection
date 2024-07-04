import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi 
ca = certifi.where()
import os
class MongoDBClient:
     client = None 
     
     def __init__(self , database_name = DATABASE_NAME) -> None:
        try:
             if MongoDBClient.client is None:
                 mongo_db_url = "mongodb+srv://jatinkumarmahaldar:jatinmahaldar@jatinkumar.7piebgt.mongodb.net/"
                 
                 MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                 self.client = MongoDBClient.client
                 self.database = self.client[database_name]
                 self.database_name = database_name
        except Exception as e:
            raise e 
             
             