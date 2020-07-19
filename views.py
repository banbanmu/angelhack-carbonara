from run import app
from flask import jsonify

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

# # auth
# # req : (username, phoneNumber, password)
# # res : (username, phoneNumber, id, token) 
# @app.route('/auth/signUp', methods=['POST'])
# def sign_up():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     phone_number = request.json.get('phoneNumber', None)
    
#     if not username:
#         return jsonify({"msg": "Missing username parameter"}), 400
#     if not password:
#         return jsonify({"msg": "Missing password parameter"}), 400
#     if not phone_number:
#         return jsonify({"msg": "Missing phoneNumber parameter"}), 400})
    
#     # save on DB

#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token), 200

# # req: (username, password)
# # res: (username, phoneNumber, id, token)
# @app.route('/auth/signIn', methods=['POST'])
# def sign_in():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400

#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     if not username:
#         return jsonify({"msg": "Missing username parameter"}), 400
#     if not password:
#         return jsonify({"msg": "Missing password parameter"}), 400

#     # password check
#     if username != 'test' or password != 'test':
#         return jsonify({"msg": "Bad username or password"}), 401

#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token), 200

# # stores
# # res : (stores)
# # store : { live : [], rest: [] }
# @app.route('/stores')
# @jwt_required
# def stores():
#     current_user = get_jwt_identity()
#     return

# # orders
# # res : (orders)
# # orders : { live: [], rest: [] }
# @app.route('/orders')
# @jwt_required
# def get_orders():
#     print('get_orders')
#     # get all the orders using token
#    pass

# # req : (storeId, menus : [menuname])
# # res : (storeId, menus : [menuname], secondsLeft, ordersLeft)
# @app.route('/order', methods=['POST'])
# @jwt_required
# def post_order():
#     print('post_orders')
#     # post an order to the db
#    pass
