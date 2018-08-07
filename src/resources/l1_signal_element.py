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

class SignalElement(Resource):

# | Field(L1)        | Field(L2) | Description                                      |
# | ---------------- | --------- | ------------------------------------------------ |
# | _id              |           | <datatime+business_type+serial_number>           |
# | satellite        |           | <satellite_id>                                   |
# | antenna_id       |           | <antenna_id_value>                               |
# | polarity         |           | <polarity_method>                                |
# | frequency        |           | <frequency_value>                                |
# | modulation_type  |           | <modulation_type_value>                          |
# | modulation_rate  |           | <modulation_rate_value>                          |
# | channel_coding   |           | <channel_coding>                                 |
# | data_source_type |           | <data_source_type> (exp.: master/vsat station)   |
# | demodulator_id   |           | <demodulator_id_value>                           |
# | time_stamp       |           | <time_stamp_value>                               |
# | frame_type       |           | <frame_type_value> (exp.: control frame/ip data) |
# | storage_path     |           | <file_storage_path>                              |
# | create           | user      | <input_user_name>                                |
# |                  | time      | <create_date_time>                               |
# | modify           | user      | <modify_user_name>                               |
# |                  | time      | <modify_date_time>                               |             |

    def __init__(self, **kwargs):
        self.mongo_cfg = kwargs['mongo_cfg']
        self.db_name = 'dev'
        self.collection_name = 'l1_signal_element'
    
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
        if result:
            return result, 201
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
        if result == True:
            return '', 200
        else:
            return '', 417

    def delete(self, data_id):
        """
        Delete a single control frame record
        """
        # TODO: delete a single data
        pass