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

# from config import load_config
from src.config import load_config
from src.resources import (
    l1_signal_element,
    l2_control_frame,
    l2_ip_data,
    l3_http,
    l3_email
)

def create_app(test_config=None):
    app = Flask(__name__)

    # Load config
    config =  load_config()
    app.config.from_object(config)

    mongo_host = app.config.get('MONGO_HOST')
    mongo_port = app.config.get('MONGO_PORT')
    mongo_db = app.config.get('MONGO_DB_NAME')
    """
    <!> 'mongo_cfg' uses 'tuple' type which can be hashed for transfering multiple arguments.
    """
    mongo_cfg = (mongo_host, mongo_port)

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    # set route for 'l1_signal_element' function
    mongo_clt = 'l1_signal_element'
    path1 = '/' + mongo_db + '/' + mongo_clt
    path2 = path1 + '/<string:data_id>'
    api.add_resource(
        l1_signal_element.SignalElement,
        path1, # '/dev/l1_signal_element',
        path2, # '/dev/l1_signal_element/<string:data_id>',
        endpoint=mongo_clt, #'l1_signal_element',
        resource_class_kwargs={'mongo_cfg': mongo_cfg}
    )
    # set route for 'l2_control_frame' function
    mongo_clt = 'l2_control_frame'
    path1 = '/' + mongo_db + '/' + mongo_clt
    path2 = path1 + '/<string:data_id>'
    api.add_resource(
        l2_control_frame.ControlFrame,
        path1, # '/dev/l2_control_frame',
        path2, # '/dev/l2_control_frame/<string:data_id>',
        endpoint=mongo_clt, # 'l2_control_frame',
        resource_class_kwargs={'mongo_cfg': mongo_cfg}
    )
    # set route for 'l2_ip_data' function
    mongo_clt = 'l2_ip_data'
    path1 = '/' + mongo_db + '/' + mongo_clt
    path2 = path1 + '/<string:data_id>'
    api.add_resource(
        l2_ip_data.IpData,
        path1, # '/dev/l2_ip_data',
        path2, # '/dev/l2_ip_data/<string:data_id>',
        endpoint=mongo_clt, # 'l2_ip_data',
        resource_class_kwargs={'mongo_cfg': mongo_cfg}
    )
    # set route for 'l3_http' function
    mongo_clt = 'l3_http'
    path1 = '/' + mongo_db + '/' + mongo_clt
    path2 = path1 + '/<string:data_id>'
    api.add_resource(
        l3_http.Http,
        path1, # '/dev/l3_http',
        path2, # '/dev/l3_http/<string:data_id>',
        endpoint=mongo_clt, # 'l3_http',
        resource_class_kwargs={'mongo_cfg': mongo_cfg}
    )
    # set route for 'l3_email' function
    mongo_clt = 'l3_email'
    path1 = '/' + mongo_db + '/' + mongo_clt
    path2 = path1 + '/<string:data_id>'
    api.add_resource(
        l3_email.Email,
        path1, # '/dev/l3_email',
        path2, # '/dev/l3_email/<string:data_id>',
        endpoint=mongo_clt, # 'l3_email',
        resource_class_kwargs={'mongo_cfg': mongo_cfg}
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

    app = create_app()

    debug = app.config.get('DEBUG')
    # RIFM(Restful Interface For MongoDB) Server IP or DNS Name
    host = app.config.get('HOST')
    # RIFM(Restful Interface For MongoDB) Server Port
    port = app.config.get('PORT')

    app.run(host, port, debug)