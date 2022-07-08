
from operator import is_
from tkinter import E
import e,sys
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import os

class DataValidation:
        ##whatever artifact I got from data ingestion I have to accept it in data validation):

   def __init__(self,data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact):

        try:
            self.data_validation_config = data_validationn_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise HousingException(e,sys) from e

   def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if train and test file is avaialbe")
            is_tarin_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_tarin_file_exist = os.path.exists(train_file_path)
            is_test_file_exist= os.path.exists(test_file_path)


            ##check the things if they are actuaaly available

            is_available =  train_file_path and test_file_path
            logging.info(f"Is train and test file exists?-> {is_available}")
            return is_available

        except Exception as e:
            raise HousingException(e,sys) from  e

   def validate_dataset_schema(self)->bool:
        try:
            
            validation_status = False
            ## Assignment validate training and testing dataset using schema file
            # 1 NUmber of columns
            # 2 Check the value of ocean proximity
            # acceptable values 
            # < 1H Ocean
            # INLAND
            # ISLAND
            # NEAR BAY
            # NEAR OCEAN
            # 3 Check columns names

            validation_status = True
            return validation_status

        except Exception as e:
            raise HousingException(e,sys) from e



   def initiate_data_validation(self):
         try :
             is_available = self.is_train_test_file_exists()

             if not is_available:
                 training_file = self.data_ingestion_artifact.train_file_path
                 testing_file =self.data_ingestion_artifact.test_file_path
                 message = f"Training file: {training_file}or Testing file : {testing_file}" \
                     "is not present"
                 logging.info(message)
                 raise Exception(message)
         except Exception as e:
             raise HousingException(e,sys) from e 





