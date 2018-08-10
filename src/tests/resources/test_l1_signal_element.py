# -*- coding: utf-8 -*-
import datetime
import random
import pytest
import json

from flask import url_for

import sys
sys.path.append('...')
from common.datetime import get_utc_datetime
from resources.l1_signal_element import SignalElement

# from ...src.common.datetime import get_utc_datetime
# from ...src.resources.l1_signal_element import SignalElement

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
    chkresponse = client.get(url_for('api.l1_signal_element'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """
    print(sys.path)
    test_id = str(get_utc_datetime()) + '_signal_element_type_' + str(random.randint(1, 9999999))
    test_post_data = {
        '_id':test_id,
        'satellite':'test_satellite_name',
        'antenna_id':'test_antenna_id_value',
        'polarity':'test_polarity_method',
        'frequency':'test_frequency_value',
        'modulation_type':'test_modulation_type_value',
        'modulation_rate':'test_modulation_rate_value',
        'channel_coding':'test_channel_coding',
        'data_source_type':'master/vsat station',
        'demodulator_id':'demodulator_id_value',
        'time_stamp':'time_stamp_value',
        'frame_type':'control-frame or ip-data',
        'storage_path': '/vol/data/signal_element/test_signal-element_file',
        'create': {
            'user':'test'
        }
    }
    chkresponse = client.post(
        url_for('api.l1_signal_element'), 
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
    test_update_id = '2018-08-06 13:04:38.845948_signal_element_type_6670346'
    test_put_data = {
        # # modify record with modify information like 'modify.user'.
        # '$set': {
        #     'satellite':'test_satellite_name',
        #     'storage_path':'/vol/data/control_frame/update_control-frame_file',
        #     'modify.user':'kowalski'
        # }
        # modify record without modify information.
        '$set': {
            'satellite':'update_satellite_name',
            'storage_path':'/vol/data/control_frame/update_signal-element_file',
        }
    }
    # You can add some fields directly
    chkresponse = client.put(
        url_for('api.l1_signal_element', data_id=test_update_id),
        json = test_put_data
    )
    # Note: How to use 'url_for', you can see this file above or Flask Quick Start.
    # assert chkresponse.status_code == 417
    assert chkresponse.status_code == 200