# -*- coding: utf-8 -*-
from flask import (
    abort,
    request,
    # json,
    # jsonify
)
from flask_restful import (
    Resource, 
    # fields, 
    # marshal_with, 
    # reqparse
)
# from bson.json_util import dumps
from src.common import dbcrud

class Ip(Resource):

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
        self.collection_name = 'l2_ip'
    
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