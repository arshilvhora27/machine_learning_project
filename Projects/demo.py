import pip
from housing.pipeline.pipeline import Pipeline, pipeline
from housing.exception import HousingException
from housing.logger import logging
def main():
    try:
        pipeline = Pipeline
        pipeline.run_pipelineself()
    except Exception as e:
        logging.error("{e}")
        print(e)

if __name__=="__main__":
    main()
     
