## What it is about
APIs for customers  
It deals with customer orders, stores, and user credentials.

## Env
envs needed
```
jwt_secret //secret_key_for_jwt
mongo //mongo_db_endpoint
livelisturl // livestoresendpoint
FLASK_APP //flask entrypoint
```
python3  
flask
ubuntu16.04  
AWS  
*nondocker*

## Install

pip install -r req.txt
pip install requests json

## Run

### dev
`nohup flask run --host=0.0.0.0`
### prod
https://flask.palletsprojects.com/en/1.1.x/deploying/
any option is ok
