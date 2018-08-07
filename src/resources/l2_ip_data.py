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

from src.common import (
    datetime,
    dbcrud,
    dtcheck
)

class IpData(Resource):
    
# | Field(L1)    | Field(L2) | Description                            |
# | ------------ | --------- | -------------------------------------- |
# | _id          |           | <datatime+business_type+serial_number> |
# | encrypted    |           | <y/n>                                  |
# | 1st_layer_ip | protocol  | <network_protocol>                     |
# |              | src_ip    | <src_ip>                               |
# |              | dst_ip    | <dst_ip>                               |
# |              | src_port  | <src_port>                             |
# |              | dst_port  | <dst_port>                             |
# | 2nd_layer_ip | protocol  | <network_protocol>                     |
# |              | src_ip    | <src_ip>                               |
# |              | dst_ip    | <dst_ip>                               |
# |              | src_port  | <src_port>                             |
# |              | dst_port  | <dst_port>                             |
# | 3rd_layer_ip | protocol  | <network_protocol>                     |
# |              | src_ip    | <src_ip>                               |
# |              | dst_ip    | <dst_ip>                               |
# |              | src_port  | <src_port>                             |
# |              | dst_port  | <dst_port>                             |
# | storage_path |           | <file_storage_path>                    |
# | create       | user      | <create_user_name>                     |
# |              | time      | <create_date_time>                     |
# | modify       | user      | <modify_user_name>                     |
# |              | time      | <modify_date_time>                     |                  |

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
        self.collection_name = 'l2_ip_data'
    
    def post(self):
        """
        Create single ip data record
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
            return result, 201
        else:
            return '', 417

    def get(self, data_id):
        """
        Get ip data record
        """
        if data_id is None:
            # TODO: return list of data
            pass
        else:
            # TODO: expose a single data
            pass

    def put(self, data_id):
        """
        Update a single ip data record
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
        if result == True:
            return '', 200
        else:
            return '', 417

    def delete(self, data_id):
        """
        Delete a single ip data record
        """
        # TODO: delete a single data
        pass