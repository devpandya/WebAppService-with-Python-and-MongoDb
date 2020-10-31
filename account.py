from flask import Blueprint

from configfile import mongo

# from configfile import not_found

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify, request

from werkzeug.security import generate_password_hash, check_password_hash

account_api = Blueprint('account_api', __name__)

# Registration Api
@account_api.route('/register_user', methods =['POST'])
def register_user():
    request_json= request.json

    if request_json is None or request_json['user']['email'] is None or request_json['user']['mobile'] is None or request_json['user']['password'] is None:
        response= jsonify({"ErrorCode": 601,"ErrorDescription":"Invalid Data",})
        response.status_code = 601
        return response
    
    existing_user = mongo.db.Users.find_one({'email': request_json['user']['email']})
    if existing_user is not None:
        response= jsonify({"ErrorCode": 602,"ErrorDescription":"User already Exists",})
        response.status_code = 602
        return response

    id = mongo.db.Users.insert(request_json['user'])
    resp = jsonify({"ErrorCode":200,"ErrorDescription":"User Registered Successfully","_id":id})
    resp.status_code = 200
    return resp


