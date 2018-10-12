# -*- coding: utf-8 -*-
import os

from flask import (
    Flask,
    Blueprint
)
from flask_restful import (
    Api,
    Resource
)
from flask_pymongo import PyMongo

from config import load_config
from common import database
from resources import (
    signal_element,
    control_frame,
    ip_data,
    http,
    email
)

def create_app(config):
    """
    Create and configure a new app instance
    """
    app = Flask(__name__)

    # set resource with blueprint for this app
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)
    # get database name
    db_name = config.MONGO_DB_NAME
    # set route for 'signal_element' function
    mongo_clt = 'signal_element'
    path1 = '/' + db_name + '/' + mongo_clt
    path2 = path1 + '/<string:id>'
    api.add_resource(
        signal_element.SignalElement,
        path1, # '/<db_name>/signal_element',
        path2, # '/<db_name/signal_element/<string:id>',
        endpoint=mongo_clt, #'signal_element',
        # resource_class_kwargs={'mongo_cfg': mongo}
    )
    # set route for 'control_frame' function
    mongo_clt = 'control_frame'
    path1 = '/' + db_name + '/' + mongo_clt
    path2 = path1 + '/<string:id>'
    api.add_resource(
        control_frame.ControlFrame,
        path1, # '/dev/control_frame',
        path2, # '/dev/control_frame/<string:id>',
        endpoint=mongo_clt, # 'control_frame',
    )
    # set route for 'ip_data' function
    mongo_clt = 'ip_data'
    path1 = '/' + db_name + '/' + mongo_clt
    path2 = path1 + '/<string:id>'
    api.add_resource(
        ip_data.IpData,
        path1, # '/dev/ip_data',
        path2, # '/dev/ip_data/<string:id>',
        endpoint=mongo_clt, # 'ip_data',
    )
    # set route for 'http' function
    mongo_clt = 'http'
    path1 = '/' + db_name + '/' + mongo_clt
    path2 = path1 + '/<string:id>'
    api.add_resource(
        http.Http,
        path1, # '/dev/http',
        path2, # '/dev/http/<string:id>',
        endpoint=mongo_clt, # 'http',
    )
    # set route for 'email' function
    mongo_clt = 'email'
    path1 = '/' + db_name + '/' + mongo_clt
    path2 = path1 + '/<string:id>'
    api.add_resource(
        email.Email,
        path1, # '/dev/email',
        path2, # '/dev/email/<string:id>',
        endpoint=mongo_clt, # 'email',
    )
    # Note:
    # 'Endpoints':
    # Many times in an API, your resource will have multiple URLs.
    # You can pass multiple URLs to the 'add_resource()' method on the Api object. 
    # Each one will be routed to your 'Resource'

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
    # get config
    cfg = load_config()
    # create app
    app = create_app(cfg)
    # set operater for mongodb
    database.mongo.init_app(app, cfg.MONGO_URI)
    # run application
    app.run(
        cfg.HOST,
        cfg.PORT,
        cfg.DEBUG
    )