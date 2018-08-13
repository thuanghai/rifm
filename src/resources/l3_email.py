# -*- coding: utf-8 -*-
from flask import (
    abort,
    request,
    json,
    jsonify
)
from flask_restful import (
    Resource, 
    # fields, 
    # marshal_with, 
    # reqparse
)

from common import (
    datetime,
    dbcrud,
    dtcheck
)

class Email(Resource):

# | Field(L1)       | Field(L2) | Description                            |
# | --------------- | --------- | -------------------------------------- |
# | _id             |           | <datatime+business_type+serial_number> |
# | title           |           | <email_title>                          |
# | from            |           | <from_address>                         |
# | to              |           | <to_address>                           |
# | attachment_tpye |           | <attachment_type> (exp.:pdf)           |
# | storage_path    |           | <file_storage_path>                    |
# | create          | user      | <create_user_name>                     |
# |                 | time      | <create_date_time>                     |
# | modify          | user      | <modify_user_name>                     |
# |                 | time      | <modify_date_time>                     |

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
        self.collection_name = 'l3_email'

    def post(self):
        """
        Create single emaile record
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
        if result:
            return 'Create success！ ID:' + result, 201
        else:
            return 'Create failed!', 417

    def get(self, data_id):
        """
        Get email record
        """
        if data_id is None:
            # TODO: return list of data
            pass
        else:
            # TODO: expose a single data
            pass

    def put(self, data_id):
        """
        Update a single email record
        """
        if request.method != 'PUT':
            abort(405)
        # check and add update time
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
        # self.mongo_cfg[0] is mongodb server host
        # self.mongo_cfg[1] is mongodb server port
        result = dbcrud.delete_one(
            self.mongo_cfg,
            self.db_name,
            self.collection_name,
            data_id)
        if result == 1:
            return 'Delete success!', 200
        else:
            return 'Delete failed！', 417