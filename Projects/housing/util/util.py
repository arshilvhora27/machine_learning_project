## so now we are going to create a function to read yaml file
import yaml
from housing.exception import HousingException
import os,sys
def read_yanl_file(file_path:str)->dict:
    """"
    Read a yaml file and return the contents as a dictionar.
    file_path:str
    """

    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e