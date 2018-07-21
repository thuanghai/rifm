# -*- coding: utf-8 -*-
from flask import (
    abort,
    request
)
from flask_restful import (
    Resource
)
# from bson.json_util import dumps
from src.common import dbcrud

class ControlFrame(Resource):

    # | DB Field Name | Description                                          |
    # | ------------- | ---------------------------------------------------- |
    # | number        | <datatime+business_type+serial_number>               |
    # | type          | <frame_type> (exp.:0xDC,0xDD,0x40,6 bytes frame,...) |
    # | file_path     | <file_storage_path>                                  |
    # | input_user    | <input_user_name>                                    |
    # | input_time    | <input_date_time>                                    |

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
        self.collection_name = 'l2_control_frame'
    
    def post(self):
        if request.method != 'POST':
            abort(405)
        
        data = request.get_json()
        # write to database
        # self.mongo_cfg[0] is mongodb server host
        # self.mongo_cfg[1] is mongodb server port
        result = dbcrud.create_one(
            self.mongo_cfg,
            self.db_name,
            self.collection_name,
            data)
        if result.acknowledged == True:
            return '', 201
        else:
            return '', 417