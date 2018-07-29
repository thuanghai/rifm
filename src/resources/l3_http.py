# -*- coding: utf-8 -*-
from flask import (
    abort,
    request,
    json,
    jsonify
)
from flask_restful import (
    Resource, 
    fields, 
    marshal_with, 
    reqparse
)
from bson.json_util import dumps
from werkzeug import exceptions

from src.common import (
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

    # | DB Field Name | Description                            |
    # | ------------- | -------------------------------------- |
    # | _id           | <datatime+business_type+serial_number> |
    # | type          | <file_type>                            |
    # | title         | <page_title>                           |
    # | file_path     | <file_storage_path>                    |
    # | input_user    | <input_user_name>                      |
    # | input_time    | <input_date_time>                      |

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
        self.collection_name = 'l3_http'
    
    # @marshal_with(person_fields)
    def post(self):
        if request.method != 'POST':
            abort(405)
        
        # data = request.get_json()
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
        if data_id is None:
            # TODO: return list of data
            pass
        else:
            # TODO: expose a single data
            pass

    def put(self, data_id):
        """
        Update a single record
        """
        if request.method != 'PUT':
            abort(405)

        # data = request.get_json()
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
        # TODO: delete a single data
        pass