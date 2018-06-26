'''
 * @Author: mikey.zhaopeng 
 * @Date: 2018-05-22 17:45:39 
 * @Last Modified by:   mikey.zhaopeng 
 * @Last Modified time: 2018-05-22 17:45:39 
'''
# -*- coding: utf-8 -*-
import os

from flask import (
    Flask,
    Blueprint
)
from flask_restful import (
    Api,
    Resource,
)
# from flask_pymongo import PyMongo

# from resources.person import(
#     Person
# )

from config import load_config

from src.resources.app_mail import AppMail

def create_app(test_config=None):
    app = Flask(__name__)

    # Load config
    config =  load_config()
    app.config.from_object(config)

    mongo_host = app.config.get('MONGO_HOST')
    mongo_port = app.config.get('MONGO_PORT')
    """
    <!> 'mongo_cfg' uses 'tuple' type which can be hashed for transfering multiple arguments.
    """
    mongo_cfg = (mongo_host, mongo_port)

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    # api.add_resource(Person, '/demo/person', endpoint="persion")
    # api.add_resource(
    #     Person, 
    #     '/demo/person', 
    #     '/demo/person/<string:id>', 
    #     endpoint="persion")
    api.add_resource(
        AppMail,
        '/tmp/app_mail',
        '/tmp/app_mail/<string:id>',
        endpoint='app_mail',
        resource_class_kwargs={'mongo_cfg': mongo_cfg}
    )

    app.register_blueprint(api_bp)

    return app

# In Flask using command in terminal
# > export FLASK_APP=src/app.py
# > export FLASK_ENV=development (option)
# > flask run -host:8000

# In Flask-Restful using below to run application 
if __name__ == '__main__':
    # set os mode
    os.environ['MODE'] = 'DEVELOPMENT'

    app = create_app()

    debug = app.config.get('DEBUG')
    # RIFM(Restful Interface For MongoDB) Server IP or DNS Name
    host = app.config.get('HOST')
    # RIFM(Restful Interface For MongoDB) Server Port
    port = app.config.get('PORT')

    app.run(host, port, debug)