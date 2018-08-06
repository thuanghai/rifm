# -*- coding: utf-8 -*-
from flask import (
    abort,
    request
)
from flask_restful import (
    Resource
)

from src.common import (
    datetime,
    dbcrud,
    dtcheck
)

class ControlFrame(Resource):

# | Field(L1)    | Field(L2) | Description                                          |
# | ------------ | --------- | ---------------------------------------------------- |
# | _id          |           | <datatime+business_type+serial_number>               |
# | type         |           | <frame_type> (exp.:0xDC,0xDD,0x40,6 bytes frame,...) |
# | storage_path |           | <file_storage_path>                                  |
# | create       | name      | <create_user_name>                                   |
# |              | time      | <create_date_time>                                   |
# | modify       | name      | <modify_date_time>                                   |
# |              | time      | <modify_date_time>                                   |                                 |

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
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
        # self.mongo_cfg[0] is mongodb server host
        # self.mongo_cfg[1] is mongodb server port
        result = dbcrud.update_one(
            self.mongo_cfg,
            self.db_name,
            self.collection_name,
            data,
            data_id)
        if result.acknowledged == True:
            return '', 200
        else:
            return '', 417

    def delete(self, data_id):
        """
        Delete a single control frame record
        """
        # TODO: delete a single data
        pass