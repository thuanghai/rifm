# -*- coding: utf-8 -*-
import datetime
import random
import pytest
import json

from flask import url_for

from src.common.datetime import get_utc_datetime
from src.resources.l3_email import Email

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
    chkresponse = client.get(url_for('api.l3_email'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """
    # get current time
    test_src_id = str(get_utc_datetime()) + '_src-type_' + 'src-serial_number'
    test_id = str(get_utc_datetime()) + '_email_type_' + str(random.randint(1, 9999999))
    test_from = "sendname@dev.org"
    test_to = "recv@dev.org"
    test_title = 'test-email-title'
    test_file_path = "/vol/data/test_file"
    test_post_data = {
        '_id' : test_id,
        'src_id': test_src_id,
        'from': test_from,
        'to': test_to,
        'title': test_title,
        'storage_path': test_file_path,
        'create': {
            'user':'test'
        }
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

def test_put(client):
    """
    Test client put method for update one document
    """
    # set update document '_id'
    test_update_id = "2018-08-06 03:17:46.099849_email_type_6035886"
    test_put_data = {
        "$set": {'title':'test_update_title_0806', 'type':'test_update_type_0806', 'modify.user':'kowalski'}
        # "$set": {'title':'test_update_title', 'type':'test_update_type'}
    }
    # You can add some fields directly
    chkresponse = client.put(
        url_for('api.l3_email', data_id=test_update_id),
        json = test_put_data
    )
    # Note: How to use 'url_for', you can see this file above or Flask Quick Start.
    assert chkresponse.status_code == 200