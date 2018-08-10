# -*- coding: utf-8 -*-
import datetime
import random
import pytest
import json

from flask import url_for

import sys
sys.path.append('...')
from common.datetime import get_utc_datetime
from resources.l2_ip_data import IpData

# How to build url using 'url_for', you can see 'Flask Quick Start' or this code below:
# --------------------------------------------------------------
# from flask import Flask, url_for
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return 'index'
# @app.route('/login')
# def login():
#     return 'login'
# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(username)
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))
#
# /
# /login
# /login?next=/
# /user/John%20Doe
# --------------------------------------------------------------

def test_get(client):
    """
    Test client get method for null
    """
    chkresponse = client.get(url_for('api.l2_ip_data'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """
    test_src_id = str(get_utc_datetime()) + '_src-type_' + 'src-serial_number'
    test_id = str(get_utc_datetime()) + '_ip_data_type_' + str(random.randint(1, 9999999))
    test_post_data = {
        '_id':test_id,
        'src_id':test_src_id,
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
        'storage_path': '/vol/data/ip_data/test_ip-data_file',
        'create': {
            'user':'test'
        }
    }

    chkresponse = client.post(
        url_for('api.l2_ip_data'), 
        json = test_post_data
    )
    # Note:
    # Passing the json argument in the test_client method
    # 1. It sets the request data to the JSON-serialized object
    # 2. It sets the content type to application/json.
    # 3. You can get the JSON data from request or response with get_json.
    assert chkresponse.status_code == 201

def test_put(client):
    """
    Test client put method for update one document
    """
    # set update document '_id'
    test_update_id = '2018-08-06 03:45:08.874553_http_type_3236152'
    test_put_data = {
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
    chkresponse = client.put(
        url_for('api.l2_ip_data', data_id=test_update_id),
        json = test_put_data
    )
    # Note: How to use 'url_for', you can see this file above or Flask Quick Start.
    assert chkresponse.status_code == 200