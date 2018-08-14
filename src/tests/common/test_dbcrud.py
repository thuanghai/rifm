# -*- coding: utf-8 -*-
#
# Using this module alone you can use command below:
# > pytest test_dbcrud.py
# 
# Run special test function in the module use command below:
# > pytest test_dbcrud.py::test_<test_function_name>
# exp.:
# > pytest test_dbcrud.py::test_get_mongodb_cfg
# > pytest test_dbcrud.py::test_db_connect
# > pytest test_dbcrud.py::test_create_one
import pytest

import sys
sys.path.append('...')
from common import dbcrud

TEST_ID = 'test_document_id'

def test_db_connect():
    """
    Test mongodb connect
    """
    # chkmongo_cfg = {'host':'0.0.0.0','port':27017}
    chkmongo_cfg = (
        '0.0.0.0',
        27017
    )
    chkdb_name = 'local'
    chkdb = dbcrud.db_connect(chkmongo_cfg, chkdb_name)
    assert chkdb.name == chkdb_name

def test_create_one():
    """
    Test insert and find one document in mongodb
    """
    mongo_cfg = (
        '0.0.0.0',
        27017
    )
    mongo_db = 'dbcrud_test_db'
    mongo_collection = 'dbcrud_test_collection'
    insert_data_id = TEST_ID
    mongo_insert_document = {
        '_id':insert_data_id, 
        'name':'test_doc', 
        'description':'A test document in mongodb'
        }
    chkresult = dbcrud.create_one(
        mongo_cfg, 
        mongo_db, 
        mongo_collection, 
        mongo_insert_document
        )
    assert chkresult == insert_data_id

def test_delete_one():
    """
    Test delete one document in mongodb
    """
    mongo_cfg = (
        '0.0.0.0',
        27017
    )
    mongo_db = 'dbcrud_test_db'
    mongo_collection = 'dbcrud_test_collection'
    # Note: Delete document using 'test_create_one' result
    delete_data_id = TEST_ID
    chkresult = dbcrud.delete_one(
        mongo_cfg,
        mongo_db,
        mongo_collection,
        delete_data_id
    )
    assert chkresult == 1