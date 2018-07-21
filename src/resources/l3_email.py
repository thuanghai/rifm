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
from src.common import dbcrud

post_parser = reqparse.RequestParser()

post_parser.add_argument(
    'title',
    dest='title',
    required=True,
    help='The title of mail'
)

post_parser.add_argument(
    'from',
    dest='from',
    help='Mail send from'
)

post_parser.add_argument(
    'to',
    dest='to',
    help='Mail send to'
)

post_parser.add_argument(
    'attachment_category',
    dest='attachment_category',
    help='Category of mail attachment'
)

person_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'from': fields.String,
    'to': fields.String,
    'attacthment_category': fields.String,
    'date_created': fields.DateTime,
    'date_updated': fields.DateTime,
}

class Email(Resource):

    # | DB Field Name   | Description                            |
    # | --------------- | -------------------------------------- |
    # | number          | <datatime+business_type+serial_number> |
    # | title           | <email_title>                          |
    # | from            | <from_address>                         |
    # | to              | <to_address>                           |
    # | attachment_tpye | <attachment_type> (exp.:pdf)           |
    # | file_path       | <file_storage_path>                    |
    # | input_user      | <input_user_name>                      |
    # | input_time      | <input_date_time>                      |

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
        self.collection_name = 'l3_email'
    
    def get(self):
        if request.method != 'GET':
            abort(405)

        # result = dbcrud.find_one(self.db_name, self.collection_name, id)
        # if result == None:
        #     return 'NULL', 204
        # else:
        #     return dumps(result), 200
        return '', 200

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