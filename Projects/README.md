# machine_learning_project
This is mymachine learning project
Heroku_Email : anvhora@shockers.wichita.edu
Heroku_api_key : 2a001397-a335-469c-8f1b-d42e337cff97
Heroku_app_name : ml-full-first-deployment




BUILD DOCKER IMAGE
'''
docker build -t <image_name>: <tagname> .

> Note : Image name for docker must be lowercase

To list docker image
''' docker images
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 84d0d9501ad9 
''' 
To check running containers in docker
'''
docker ps 
'''
To stop docker container 
''' 
docker stop <container_id>
'''