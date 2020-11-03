from flask import Blueprint

from configfile import mongo

from bson.json_util import dumps

from flask import jsonify, request


master_api = Blueprint('master_api', __name__)

@master_api.route('/getmaster', methods=['GET'])
def get_master_data():
     Resources = mongo.db.Resources.find({},{'_id':False} )
     Features = mongo.db.Features.find({"isactive":True},{'_id':False} )
     master_data=jsonify({"Resources": list(Resources), "Features":list(Features)})
     master_data.status_code = 200
     return master_data