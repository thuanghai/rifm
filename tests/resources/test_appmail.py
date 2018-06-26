# -*- coding: utf-8 -*-
import pytest
import json

from flask import url_for
from src.resources.app_mail import AppMail

def test_get(client):
    """
    Test client get method for null
    """
    chkresponse = client.get(url_for('api.app_mail'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """
    test_post_data = {
        'name' : 'test_name',
        'description': 'A test document in mongodb'
    }

    chkresponse = client.post(
        url_for('api.app_mail'), 
        json = test_post_data
    )
    # Note:
    # Passing the json argument in the test_client method
    # 1. It sets the request data to the JSON-serialized object
    # 2. It sets the content type to application/json.
    # 3. You can get the JSON data from request or response with get_json.
    assert chkresponse.status_code == 201