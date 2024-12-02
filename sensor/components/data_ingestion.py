from sensor.logger import logging
from sensor.exception import SensorException
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
import os , sys
from sklearn.model_selection import train_test_split
from pandas import DataFrame
from sensor.data_access.sensor_data import SensorData
from sensor.constant import training_pipeline
class DataIngestion:
    def __init__(self , data_ingestion_config : DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)
            
    def export_data_into_feature_store(self): 
        try:
            logging.info("exporting data into feature store")
            sensor_data = SensorData()
            dataframe  = sensor_data.export_collection_as_dataframe(colllection_name=self.data_ingestion_config.collection_name)
            feature_store_file_path = self.data_ingestion_config.feature_store
            
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index = False,header=True)
            return dataframe 
        except Exception as e:
            raise SensorException(e,sys)
               
    def split_data_as_train_test_split(self , DataFrame):
        try:
            train_set , test_set = train_test_split(DataFrame, test_size = self.data_ingestion_config.train_test_split_ratio)
            logging.info("performed train test split in dataframe")
            dir_path  = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info("exporting file into train and test file path")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index = False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index = False,header=True)
            
        except Exception as e:
            raise SensorException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test_split(DataFrame=dataframe)
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=self.data_ingestion_config.training_file_path, 
                                                              test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
            
        except Exception as e:
            raise SensorException(e,sys)