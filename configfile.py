from flask import Flask

from flask_cors import CORS

from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.secret_key = "webappv1"

    app.config['MONGO_URI'] = "mongodb://localhost:27017/ReFlaMo"

    # INIT EXTENSIONS ----------------------
    mongo.init_app(app)

    return app

