# -*- coding: utf-8 -*-
from flask import (
    abort,
    request
)
from flask_restful import (
    Resource
)

from common import (
    datetime,
    dbcrud,
    dtcheck
)

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
        mongo_cfg = kwargs['mongo_cfg']
        self.db_host = mongo_cfg[0]
        self.db_port = mongo_cfg[1]
        self.db_name = mongo_cfg[2]
        self.collection_name = 'l2_control_frame'
    
    def post(self):
        """
        Create single control frame data record
        """
        if request.method != 'POST':
            abort(405)
        # check and add create time
        data = dtcheck.check_create(request.get_json())
        # write to database
        result = dbcrud.create_one(
            self.db_host,
            self.db_port,
            self.db_name,
            self.collection_name,
            data)
        if result:
            return 'Create success！ ID:' + result, 201
        else:
            return 'Create failed!', 417

    def get(self, data_id):
        """
        Get control frame data record
        """
        if data_id is None:
            # TODO: return list of data
            pass
        else:
            # TODO: expose a single data
            pass

    def put(self, data_id):
        """
        Update a single control frame data record
        """
        if request.method != 'PUT':
            abort(405)
        # check and update time
        data = dtcheck.check_modify(request.get_json())
        # write to database
        result = dbcrud.update_one(
            self.db_host,
            self.db_port,
            self.db_name,
            self.collection_name,
            data,
            data_id)
        if result == True:
            return 'Update success!', 200
        else:
            return 'Update failed！', 417

    def delete(self, data_id):
        """
        Delete a single control frame record
        """
        if request.method != 'DELETE':
            abort(405)
        # write to database
        result = dbcrud.delete_one(
            self.db_host,
            self.db_port,
            self.db_name,
            self.collection_name,
            data_id)
        if result == 1:
            return 'Delete success!', 200
        else:
            return 'Delete failed！', 417