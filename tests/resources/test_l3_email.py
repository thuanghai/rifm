# -*- coding: utf-8 -*-
import datetime
import random
import pytest
import json

from flask import url_for
from src.resources.l3_email import Email

def test_get(client):
    """
    Test client get method for null
    """
    chkresponse = client.get(url_for('api.l3_email'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """
    # get current time
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    test_number = str(nowTime) + '-test_business_type-' + str(random.randint(1, 9999999))
    test_from = "sendname@dev.org"
    test_to = "recv@dev.org"
    test_title = 'test-email-title'
    test_file_path = "/vol/data/test_file"
    test_post_data = {
        'number' : test_number,
        'from': test_from,
        'to': test_to,
        'title': test_title,
        'file_path': test_file_path,
        'write_person': 'test_persion_name',
        'write_time': nowTime
    }

    chkresponse = client.post(
        url_for('api.l3_email'), 
        json = test_post_data
    )
    # Note:
    # Passing the json argument in the test_client method
    # 1. It sets the request data to the JSON-serialized object
    # 2. It sets the content type to application/json.
    # 3. You can get the JSON data from request or response with get_json.
    assert chkresponse.status_code == 201