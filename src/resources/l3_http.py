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

# post_parser = reqparse.RequestParser()

# post_parser.add_argument(
#     'name',
#     dest='name',
#     required=True,
#     help='The name of person',
# )

# post_parser.add_argument(
#     'sex',
#     dest='sex',
#     help='The sex of person',
# )

# post_parser.add_argument(
#     'birth',
#     dest='birth',
#     help='The birthday of person',
# )

# person_fields = {
#     'id': fields.Integer,
#     'name': fields.String,
#     'sex': fields.String,
#     'birth': fields.DateTime,
#     'date_created': fields.DateTime,
#     'date_updated': fields.DateTime,
# }

class Http(Resource):

# | Field (L1)   | Field (L2) | Description                        |
# | ------------ | ---------- | ---------------------------------- |
# | _id          |            | <time+business_type+serial_number> |
# | src_id       |            | <ip_data_id>                       |
# | title        |            | <http_page_title>                  |
# | type         |            | <http_file_type>                   |
# | storage_path |            | <file_storage_path>                |
# | create       | user       | <create_user_name>                 |
# |              | time       | <create_date_time>                 |
# | modify       | user       | <last_modify_user>                 |
# |              | time       | <last_modify_time>                 |

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
        self.collection_name = 'l3_http'
    
    # @marshal_with(person_fields)
    def post(self):
        """
        Create a single http record
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
        Get http record
        """
        if data_id is None:
            # TODO: return list of data
            pass
        else:
            # TODO: expose a single data
            pass

    def put(self, data_id):
        """
        Update a single http record
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