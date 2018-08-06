# -*- coding: utf-8 -*-
import random
import pytest
import json

from flask import url_for

from src.common.datetime import get_utc_datetime
from src.resources.l3_http import Http

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
    chkresponse = client.get(url_for('api.l3_http'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """
    # get current time
    test_src_id = str(get_utc_datetime()) + '_src-type_' + 'src-serial_number'
    test_id = str(get_utc_datetime()) + '_http_type_' + str(random.randint(1, 9999999))
    test_title = 'test-http-title'
    test_type = 'test-http-file-type'
    test_path = "/vol/data/test_http_file"
    test_post_data = {
        '_id' : test_id,
        'src_id': test_src_id,
        'title': test_title,
        'type': test_type,
        'storage_path': test_path,
        'create': {
            'user':'test'
        }
    }

    chkresponse = client.post(
        url_for('api.l3_http'), 
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
    test_update_id = "2018-07-29 14:27:15.199516_http_type_3235623"
    test_put_data = {
        "$set": {'title':'test_update_title_0729', 'type':'test_update_type_0729', 'modify.user':'kowalski'}
        # "$set": {'title':'test_update_title', 'type':'test_update_type'}
    }
    # You can add some fields directly
    chkresponse = client.put(
        url_for('api.l3_http', data_id=test_update_id),
        json = test_put_data
    )
    # Note: How to use 'url_for', you can see this file above or Flask Quick Start.
    assert chkresponse.status_code == 200
