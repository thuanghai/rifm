# -*- coding: utf-8 -*-
from flask import (
    abort,
    request
)
from flask_restful import (
    Resource
)

from common import database
from common import datetime as dt

class ControlFrame(Resource):

# | Field(L1)    | Field(L2) | Description                                          |
# | ------------ | --------- | ---------------------------------------------------- |
# | _id          |           | <datatime+business_type+serial_number>               |
# | src_id       |           | <source_data_id(l1_signal_element id)>               |
# | type         |           | <frame_type> (exp.:0xDC,0xDD,0x40,6 bytes frame,...) |
# | storage_path |           | <file_storage_path>                                  |
# | time_stamp   |           | <time_stamp_value>                                   |
# | create       | name      | <create_user_name>                                   |
# |              | time      | <create_date_time>                                   |
# | modify       | name      | <modify_date_time>                                   |
# |              | time      | <modify_date_time>                                   |

    def __init__(self, **kwargs):
        self.collection = 'control_frame'
    
    def post(self):
        """
        Create single control frame data record
        """
        if request.method != 'POST':
            abort(405)
        # check and add create time
        data = dt.check_create(request.get_json())
        # write to database
        result = database.create_one(self.collection, data)
        if result:
            return "Create success！ ID:" + str(result), 201
        else:
            return "Create failed!", 417

    def get(self, id):
        """
        Get control frame data record
        """
        if request.method != 'GET':
            abort(405)
        # find document by '_id'
        result = database.find_one(self.collection, id)
        if result:
            # Note1: the type of result is <class 'dict'>
            return result, 200
        else:
            return "None!", 200

    def put(self, id):
        """
        Update a single control frame data record
        """
        if request.method != 'PUT':
            abort(405)
        # check and update time
        data = dt.check_modify(request.get_json())
        # write to database
        result = database.update_one(self.collection, id, data)
        if result == True:
            return "Update success!", 200
        else:
            return "Update failed！", 417

    def delete(self, id):
        """
        Delete a single control frame record
        """
        if request.method != 'DELETE':
            abort(405)
        # write to database
        result = database.delete_one(self.collection, id)
        if result == True:
            return "Delete success!", 200
        else:
            return "Delete failed！", 417
