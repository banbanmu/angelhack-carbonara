from flask_restful import Resource, reqparse
from run import db
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import requests
import json
import os 

# TODO parser decoupling
sup = reqparse.RequestParser()
sup.add_argument(
    'userName', help='This field cannot be blank', type=str, required=True)
sup.add_argument(
    'password', help='This field cannot be blank', type=str, required=True)
sup.add_argument(
    'phoneNumber', help='This field cannot be blank', type=str, required=True)
sup.add_argument(
    'address', help='This field cannot be blank', type=str, required=True)


class UserRegistration(Resource):
    def post(self):
        d = sup.parse_args()
        new_user = {
            'userName': d['userName'],
            'password': sha256.hash(d['password']),
            'phoneNumber': d['phoneNumber'],
            'address': d['address']
        }
        try:
            db.users.insert_one(new_user)
            access_token = create_access_token(identity=d['userName'])
            refresh_token = create_refresh_token(identity=d['userName'])
            return {
                'message': 'User {} was created'.format(d['userName']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


sip = reqparse.RequestParser()
sip.add_argument(
    'userName', help='This field cannot be blank', type=str, required=True)
sip.add_argument(
    'password', help='This field cannot be blank', type=str, required=True)


class UserLogin(Resource):
    def post(self):
        d = sip.parse_args()
        u = db.users.find_one({"userName": d['userName']})
        if not u:
            return {'message': 'User {} doesn\'t exist'.format(d['userName'])}
        v = sha256.verify(d['password'], u['password'])
        if v:
            access_token = create_access_token(identity=d['userName'])
            refresh_token = create_refresh_token(identity=d['userName'])
            return {
                'message': 'Logged in as {}'.format(u['userName']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class AllStores(Resource):
    @jwt_required
    def get(self):
        url = os.environ['livelisturl']
        l = requests.get(url).content
        l = json.loads(l)
        ss = list(db.store.find({}))
        return {'stores': {
            'live': l,
            'all': list(ss),
        }}


class AllOrders(Resource):
    @jwt_required
    def get(self):
        liveOrders = db.order.find({'state': 'STARTED'}, {'_id': 0})
        restOrders = db.order.find({'state': {'$ne': 'STARTED'}}, {'_id': 0})
        return {'orders': {
            'started': list(liveOrders),
            'rest': list(restOrders),
        }}


pop = reqparse.RequestParser()
pop.add_argument(
    'storeId', help='This field cannot be blank', type=int, required=True)
pop.add_argument(
    'menuName', help='This field cannot be blank', type=str, required=True)


class OrderCreate(Resource):
    @jwt_required
    def post(self):
        d = pop.parse_args()
        uname = get_jwt_identity()
        u = db.users.find_one({'userName': uname})
        new_order = {
            'storeId': d['storeId'],
            'menuName': d['menuName'],
            'address': u['address'],
            'phonNumber': u['phoneNumber'],
            'state': 'NOT_STARTED',
            'userId': str(u['_id'])
        }
        db.orders.insert_one(new_order)
        new_order['_id'] = str(new_order['_id'])
        return new_order
