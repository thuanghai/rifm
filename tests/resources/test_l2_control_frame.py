# -*- coding: utf-8 -*-
import datetime
import random
import pytest
import json

from flask import url_for
from src.resources.l2_ip_data import IpData

def test_get(client):
    """
    Test client get method for null
    """
    chkresponse = client.get(url_for('api.l2_control_frame'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """
    # get current time
    nowTime = str(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
    test_number = nowTime + '_type_' + str(random.randint(1, 9999999))
    test_post_data = {
        'number' : test_number,
        'type': '0xDD',
        "file_path":"test_file_path",
        "input_user":"test_kowalski",
        "input_time": nowTime
    }
    chkresponse = client.post(
        url_for('api.l2_control_frame'), 
        json = test_post_data
    )
    # Note:
    # Passing the json argument in the test_client method
    # 1. It sets the request data to the JSON-serialized object
    # 2. It sets the content type to application/json.
    # 3. You can get the JSON data from request or response with get_json.
    assert chkresponse.status_code == 201