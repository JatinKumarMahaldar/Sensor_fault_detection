from sensor.configuration.mongo_db_connections import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
from sensor.entity.config_entity import TrainingPipelineConfig , DataIngestionConfig

    
if __name__ == '__main__':
    TrainingPipelineConfig = TrainingPipelineConfig()
    DataIngestionConfig = DataIngestionConfig(training_pipeline_config =TrainingPipelineConfig)
    print(DataIngestionConfig.__dict__)
    
    
    
    
    
"""
    mongo_db_client = MongoDBClient()
    print(mongo_db_client.client)
    print(mongo_db_client.database)
    print(mongo_db_client.database_name)""" 