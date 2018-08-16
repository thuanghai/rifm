# -*- coding: utf-8 -*-

import pytest

import sys
sys.path.append('...')
from common import dbcrud

TEST_ID = 'test_document_id'

def test_db_connect():
    """
    Test mongodb connect
    """
    chk_db_host = '0.0.0.0'
    chk_db_port = 27017
    chk_db_name = 'local'
    chkdb = dbcrud.db_connect(chk_db_host, chk_db_port, chk_db_name)
    assert chkdb.name == chk_db_name

def test_create_one():
    """
    Test insert and find one document in mongodb
    """
    db_host = '0.0.0.0'
    db_port = 27017
    db_name = 'dbcrud_test_db'
    db_collection = 'dbcrud_test_collection'
    insert_data_id = TEST_ID
    insert_document = {
        '_id':insert_data_id, 
        'name':'test_doc', 
        'description':'A test document in mongodb'
        }
    chkresult = dbcrud.create_one(
        db_host, 
        db_port,
        db_name, 
        db_collection, 
        insert_document
        )
    assert chkresult == insert_data_id

def test_delete_one():
    """
    Test delete one document in mongodb
    """
    db_host = '0.0.0.0'
    db_port = 27017
    db_name = 'dbcrud_test_db'
    db_collection = 'dbcrud_test_collection'
    delete_data_id = TEST_ID
    chkresult = dbcrud.delete_one(
        db_host, 
        db_port,
        db_name, 
        db_collection, 
        delete_data_id
    )
    assert chkresult == 1