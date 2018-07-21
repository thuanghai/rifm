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
    chkresponse = client.get(url_for('api.l2_ip_data'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """

    # get current time
    nowTime = str(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
    test_number = nowTime + '-test_business_type-' + str(random.randint(1, 9999999))
    test_post_data = {
        'number' : test_number,
        'encrypted': 'n',
        '1st_layer_ip': {
            "protocol":"ip",
            "src_ip":"127.0.0.1",
            "dst_ip":"127.0.0.1",
            "src_port":"4004",
            "dst_port":"4004"
        },
        "2nd_layer_ip": {
            "protocol":"tcp",
            "src_ip":"192.168.1.101",
            "dst_ip":"192.168.1.102",
            "src_port":"10001",
            "dst_port":"10002"
        },
        "3rd_layer_ip": {
            "protocol":"ip",
            "src_ip":"192.168.2.201",
            "dst_ip":"192.168.2.202",
            "src_port":"20001",
            "dst_port":"20002"
        },
        "file_path":"test_file_path",
        "input_user":"test_kowalski",
        "input_time": nowTime
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