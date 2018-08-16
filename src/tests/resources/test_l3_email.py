# -*- coding: utf-8 -*-
import datetime
import random
import pytest
import json

from flask import url_for

import sys
sys.path.append('...')
from common.datetime import get_timestamp
from resources.l3_email import Email

class TestL1SignalElement():
    # document '_id' in mongodb during the test
    __test_id = 'test_l3_email-' + str(get_timestamp())

    def test_post(self, client):
        """
        Test client post method for insert one document
        """
        insert_id = self.__test_id
        insert_src_id = 'test_src_id-' + insert_id
        insert_data = {
            '_id':insert_id,
            'src_id':insert_src_id,
            'from':'sendname@dev.org',
            'to':'recv@dev.org',
            'title':'test-email-title',
            'storage_path':'/vol/data/email/test_email_file',
            'time_stamp':'input_your_time_stamp',
            'create': {
                'user':'test'
            }
        }
        # test client request with 'POST' method
        chkresponse = client.post(
            url_for('api.l3_email'), 
            json = insert_data
        )
        # Note:
        # Passing the json argument in the test_client method
        # 1. It sets the request data to the JSON-serialized object
        # 2. It sets the content type to application/json.
        # 3. You can get the JSON data from request or response with get_json.
        assert chkresponse.status_code == 201

<<<<<<< HEAD
def test_post(client):
    """
    Test client post method for insert one document
    """
    test_src_id = str(get_utc_datetime()) + '_src-type_' + 'src-serial_number'
    test_id = str(get_utc_datetime()) + '_email_type_' + str(random.randint(1, 9999999))
    test_post_data = {
        '_id':test_id,
        'src_id':test_src_id,
        'from':'sendname@dev.org',
        'to':'recv@dev.org',
        'title':'test-email-title',
        'storage_path':'/vol/data/email/test_email_file',
        'time_stamp':'input_your_time_stamp',
        'create': {
            'user':'test'
=======
    def test_get(self, client):
        """
        Test client get method for null
        """
        # set read document '_id'
        find_id = self.__test_id
        # test client request with 'GET' method 
        chkresponse = client.get(url_for('api.l3_email', data_id = find_id))
        assert chkresponse.status_code == 200

    def test_put(self, client):
        """
        Test client put method for update one document
        """
        # set update document '_id'
        update_id = self.__test_id
        update_data = {
            # # modify record with modify information like 'modify.user'.
            # '$set':{
            #     'title':'test_update_title_0806',
            #     'type':'test_update_type_0806',
            #     'modify.user':'update_user'
            #     }
            # modify record without modify information.
            "$set":{
                'title':'test_update_title',
                'type':'test_update_type'
                }
>>>>>>> dev
        }
        # You can add some fields directly

        # test client request with 'PUT' method
        chkresponse = client.put(
            url_for('api.l3_email', data_id = update_id),
            json = update_data
        )
        # Note: How to use 'url_for', you can see this file above or Flask Quick Start.
        assert chkresponse.status_code == 200

<<<<<<< HEAD
def test_put(client):
    """
    Test client put method for update one document
    """
    # set update document '_id'
    test_update_id = '2018-08-06 03:17:46.099849_email_type_6035886'
    test_put_data = {
        # # modify record with modify information like 'modify.user'.
        # '$set':{
        #     'title':'test_update_title_0806',
        #     'type':'test_update_type_0806',
        #     'modify.user':'update_user'
        #     }
        # modify record without modify information.
        "$set":{
            'title':'test_update_title',
            'type':'test_update_type'
            }
    }
    # You can add some fields directly
    chkresponse = client.put(
        url_for('api.l3_email', data_id=test_update_id),
        json = test_put_data
    )
    # Note: How to use 'url_for', you can see this file above or Flask Quick Start.
    assert chkresponse.status_code == 200

def test_delete(client):
    """
    Test client delete method for update one document
    """
    # set delete document '_id'
    test_delete_id = '2018-08-06 03:17:46.099849_email_type_6035886'
    chkresponse = client.delete(
        url_for('api.l3_email', data_id=test_delete_id)
    )
    assert chkresponse.status_code == 200
=======
    def test_delete(self, client):
        """
        Test client delete method for update one document
        """
        # set delete document '_id'
        delete_id = self.__test_id
        # test client request with 'DELETE' method
        chkresponse = client.delete(
            url_for('api.l3_email', data_id = delete_id)
        )
        assert chkresponse.status_code == 200
>>>>>>> dev
