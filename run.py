import os
from flask import Flask, jsonify, request
from flask_restful import Api
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# app
app = Flask(__name__)
CORS(app)
api = Api(app)

# secret
app.config['JWT_SECRET_KEY'] =  os.environ['jwt_secret']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = False
jwt = JWTManager(app)

# db
client = MongoClient(os.environ['mongo']) # TODO env
db = client.ciabatta

import views, resources

api.add_resource(resources.UserRegistration, '/auth/signUp')
api.add_resource(resources.UserLogin, '/auth/signIn')
api.add_resource(resources.TokenRefresh, '/auth/tokenRefresh')
api.add_resource(resources.AllStores, '/stores')
api.add_resource(resources.AllOrders, '/orders')
api.add_resource(resources.OrderCreate, '/order')
