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

from src.common import dbcrud

def test_db_connect():
    """
    Test mongodb connect
    """
    chkmongo_cfg = {'host': '0.0.0.0', 'port': 27017}
    chkdb_name = 'local'
    chkdb = dbcrud.db_connect(chkmongo_cfg, chkdb_name)
    assert chkdb.name == chkdb_name

def test_create_one():
    """
    Test insert and find one document in mongodb
    """
    mongo_cfg = {'host': '0.0.0.0', 'port': 27017}
    mongo_db = 'dbcrud_test_db'
    mongo_collection = 'dbcrud_test_collection'
    mongo_insert_document = {'name': 'test_doc', 'description': 'A test document in mongodb'}
    chkresult = dbcrud.create_one(mongo_cfg, mongo_db, mongo_collection, mongo_insert_document)
    assert chkresult.acknowledged == True