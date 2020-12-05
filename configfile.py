from flask import Flask

from flask_cors import CORS

from flask_pymongo import PyMongo

import urllib.parse

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.secret_key = "webappv1"

    app.config['MONGO_URI'] = "mongodb+srv://dbadmin:"+ urllib.parse.quote("H@ppydev@2002") +"@cluster0.tuyk7.mongodb.net/ReFlaMo?retryWrites=true&w=majority"

    # INIT EXTENSIONS ----------------------
    mongo.init_app(app)

    return app

