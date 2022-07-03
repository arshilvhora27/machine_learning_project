
from housing.component import data_ingestion
from housing.constant import CONFIG_FILE_PATH, CURRENT_TIME_STAMP, DATA_INGESTION_ARTIFACT_DIR, DATA_INGESTION_CONFIG_KEY, DATA_INGESTION_DIR_NAME_KEY, DATA_INGESTION_DOWNLOAD_URL_KEY, DATA_INGESTION_INGESTED_DIR_NAME_KEY, DATA_INGESTION_RAW_DATA_DIR_KEY, DATA_INGESTION_TEST_DIR_KEY, DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY, DATA_INGESTION_TRAIN_DIR_KEY, ROOT_DIR, TRAINING_PIPELINE_ARTIFACT_DIR_KEY, TRAINING_PIPELINE_CONFIG_KEY, TRAINING_PIPELINE_NAME_KEY
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelTrainerConfig, \
ModelEvaluationConfig,ModelPushConfig, TrainingPipelineConfig  
from housing.util.util import read_yanl_file
from housing.exception import HousingException 
from housing.logger import logging

from housing.constant import *

import os,sys


class Configuration:

    def __init__(self,
        config_file_path:str=CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        ) -> None:
        try:
            
            
            self.config_info = read_yanl_file(file_path=config_file_path)
            self.training_pipeline_config=self.get_training_pipeline_config()
            self.training_pipeline_config.artifact_dir
            self.time_stamp =current_time_stamp
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_data_ingestion_config(self) ->DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir 
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
        

            tgz_download_dir =os.path.join(
            data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]

            )

            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
             ) 

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
                
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]

            )
            ingested_test_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )
        except Exception as e:
            raise HousingException(e,sys) from e
            

    def get_data_validation__config(self) ->DataValidationConfig:
        pass

    def get_data_transformation__config(self) ->DataTransformationConfig:
        pass

    def get_model_trainer_config(self)->ModelTrainerConfig:
        pass

    def model_evaluation_config(self)->ModelEvaluationConfig:
        pass
    
    def model_pusher_config(self)->ModelPushConfig:
        pass

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
           training_pipeline_config =  self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
           artifact_dir = os.path.join(ROOT_DIR,
           training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
           training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]


           
           )

           training_pipeline_config =TrainingPipelineConfig(artifact_dir=artifact_dir)
           logging.info(f"Training pipeline config : {training_pipeline_config}")
           return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e  