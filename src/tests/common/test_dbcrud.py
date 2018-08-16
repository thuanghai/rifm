# -*- coding: utf-8 -*-
#
# Using this module alone you can use command below:
# > pytest test_dbcrud.py
# 
# Run special test function in the module use command below:
# > pytest test_dbcrud.py::test_<test_function_name>
# exp.:
# > pytest test_dbcrud.py::test_db_connect
# > pytest test_dbcrud.py::test_create_one
# You can add '-s' for print something writed in the code, command like this:
# > pytest test_dbcrud.py::test_delete_one -s

import pytest

import sys
sys.path.append('...')
from common import dbcrud

TEST_ID = 'test_document_id'

def test_db_connect():
    """
    Test mongodb connect
    """
<<<<<<< HEAD
    # chkmongo_cfg = {'host':'0.0.0.0','port':27017}
    chkmongo_cfg = (
        '0.0.0.0',
        27017
    )
    chkdb_name = 'local'
    chkdb = dbcrud.db_connect(chkmongo_cfg, chkdb_name)
    assert chkdb.name == chkdb_name
=======
    chk_db_host = '0.0.0.0'
    chk_db_port = 27017
    chk_db_name = 'local'
    chkdb = dbcrud.db_connect(chk_db_host, chk_db_port, chk_db_name)
    assert chkdb.name == chk_db_name
>>>>>>> dev

def test_create_one():
    """
    Test insert and find one document in mongodb
    """
<<<<<<< HEAD
    mongo_cfg = (
        '0.0.0.0',
        27017
    )
    mongo_db = 'dbcrud_test_db'
    mongo_collection = 'dbcrud_test_collection'
    insert_data_id = TEST_ID
    mongo_insert_document = {
=======
    db_host = '0.0.0.0'
    db_port = 27017
    db_name = 'dbcrud_test_db'
    db_collection = 'dbcrud_test_collection'
    insert_data_id = TEST_ID
    insert_document = {
>>>>>>> dev
        '_id':insert_data_id, 
        'name':'test_doc', 
        'description':'A test document in mongodb'
        }
    chkresult = dbcrud.create_one(
<<<<<<< HEAD
        mongo_cfg, 
        mongo_db, 
        mongo_collection, 
        mongo_insert_document
=======
        db_host, 
        db_port,
        db_name, 
        db_collection, 
        insert_document
>>>>>>> dev
        )
    assert chkresult == insert_data_id

def test_delete_one():
    """
    Test delete one document in mongodb
    """
<<<<<<< HEAD
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
=======
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
>>>>>>> dev
        delete_data_id
    )
    assert chkresult == 1