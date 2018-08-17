# -*- coding: utf-8 -*-
import datetime
import random
import pytest
import json

from flask import url_for

import sys
sys.path.append('...')
from common.datetime import get_timestamp
from resources.l2_ip_data import IpData

class TestL1SignalElement():
    # document '_id' in mongodb during the test
    __test_id = 'test_l2_ip_data-' + str(get_timestamp())

    def test_post(self, client):
        """
        Test client post method for insert one document
        """
        insert_id = self.__test_id
        insert_src_id = 'test_src_id-' + insert_id
        insert_data = {
            '_id':insert_id,
            'src_id':insert_src_id,
            'encrypted':'n',
            '1st_layer_ip':{
                'protocol':'ip',
                'src_ip':'127.0.0.1',
                'dst_ip':'127.0.0.1',
                'src_port':'4004',
                'dst_port':'4004'
            },
            '2nd_layer_ip':{
                'protocol':'tcp',
                'src_ip':'192.168.1.101',
                'dst_ip':'192.168.1.102',
                'src_port':'10001',
                'dst_port':'10002'
            },
            '3rd_layer_ip':{
                'protocol':'ip',
                'src_ip':'192.168.2.201',
                'dst_ip':'192.168.2.202',
                'src_port':'20001',
                'dst_port':'20002'
            },
            'storage_path':'/vol/data/ip_data/test_ip-data_file',
            'time_stamp':'input_your_time_stamp',
            'create': {
                'user':'test'
            }
        }
        # test client request with 'POST' method 
        chkresponse = client.post(
            url_for('api.l2_ip_data'), 
            json = insert_data
        )
        # Note:
        # Passing the json argument in the test_client method
        # 1. It sets the request data to the JSON-serialized object
        # 2. It sets the content type to application/json.
        # 3. You can get the JSON data from request or response with get_json.
        assert chkresponse.status_code == 201

    def test_get(self, client):
        """
        Test client get method for null
        """
        # set read document '_id'
        find_id = self.__test_id
        # test client request with 'GET' method 
        chkresponse = client.get(url_for('api.l2_ip_data', data_id = find_id))
        assert chkresponse.status_code == 200

    def test_put(self, client):
        """
        Test client put method for update one document
        """
        # set update document '_id'
        update_id = self.__test_id
        update_data = {
            # # modify record with modify information like 'modify.user'.
            # '$set': {
            #     'encrypted':'y', 
            #     '3rd_layer_ip.src':'172.16.3.101', 
            #     '3rd_layer_ip.dst':'172.16.3.102',
            #     'modify.user':'kowalski'
            #     }
            # modify record without modify information.
            '$set': {
                'encrypted':'n',
                '3rd_layer_ip.src':'172.16.2.101',
                '3rd_layer_ip.dst':'172.16.2.102'
            }
        }
        # You can add some fields directly

        # test client request with 'PUT' method 
        chkresponse = client.put(
            url_for('api.l2_ip_data', data_id = update_id),
            json = update_data
        )
        # Note: How to use 'url_for', you can see this file above or Flask Quick Start.
        assert chkresponse.status_code == 200

    def test_delete(self, client):
        """
        Test client delete method for update one document
        """
        # set delete document '_id'
        delete_id = self.__test_id
        # test client request with 'DELETE' method 
        chkresponse = client.delete(
            url_for('api.l2_ip_data', data_id = delete_id)
        )
<<<<<<< HEAD
        assert chkresponse.status_code == 200
=======
        assert chkresponse.status_code == 200
>>>>>>> master
