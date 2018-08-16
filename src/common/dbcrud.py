# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

def db_connect(
    # mongo_cfg: dict(type=tuple, help='MongoDB host and port'),
    db_host: dict(type=str, help='MongoDB database host'),
    db_port: dict(type=str, help='MongoDB database port'),
    db_name: dict(type=str, help='MongoDB database name')
):
    """
    Connect mongodb servery
    """
    # Make a connection with 'MongoClient'
    client =  MongoClient(db_host, db_port)
    # Get database with name 'db_name'
    db = client[db_name]
    return db

def db_close(client):
    """
    Close mongodb
    """
    # type of client is pymongo.database
    client.close()

def create_one(
    db_host: dict(type=str, help='MongoDB database host'),
    db_port: dict(type=str, help='MongoDB database port'),
    db_name: dict(type=str, help='MongoDB database name'), 
    collection_name: dict(type=str, help ='MongoDB collection name'), 
    data
):
    """
    Insert one document of mongodb
    """
    # Get database
    db = db_connect(db_host, db_port, db_name)
    # Get collection
    clt = db[collection_name]
    # Insert one document
    result = clt.insert_one(data)
    # Check write result
    if result.acknowledged == True:
        return result.inserted_id
    else:
        return ''

def find_one(
    db_host: dict(type=str, help='MongoDB database host'),
    db_port: dict(type=str, help='MongoDB database port'),
    db_name: dict(type=str, help='MongoDB database name'), 
    collection_name: dict(type=str, help='MongoDB collection name'), 
    data_id: dict(type=str, help='MongoDB document id')
):
    """
    Find one document by its '_id'
    """
    # Get database
    db = db_connect(db_host, db_port, db_name)
    # Get collection
    clt = db[collection_name]
    # Find document by 'id'
    return clt.find_one({'_id': data_id})

def update_one(
    db_host: dict(type=str, help='MongoDB database host'),
    db_port: dict(type=str, help='MongoDB database port'),
    db_name: dict(type=str, help='MongoDB database name'), 
    collection_name: dict(type=str, help='MongoDB collection name'), 
    data: dict(type=str, help='String for JSON data expression'),
    data_id: dict(type=str, help='MongoDB document id')
):
    """
    Update one document field
    """
    # Get database
    db = db_connect(db_host, db_port, db_name)
    # Get collection
    clt = db[collection_name]
    # Update and check result
    result = clt.update_one({"_id": data_id}, data)
    if (result.acknowledged == True) \
        and (result.matched_count == 1) \
        and (result.modified_count == 1):
        return True
    else:
        return False

def delete_one(
    db_host: dict(type=str, help='MongoDB database host'),
    db_port: dict(type=str, help='MongoDB database port'),
    db_name: dict(type=str, help='MongoDB database name'), 
    collection_name: dict(type=str, help ='MongoDB collection name'), 
    data_id: dict(type=str, help='MongoDB document id')
):
    # Get database
    db = db_connect(db_host, db_port, db_name)
    # Get collection
    clt = db[collection_name]
    # Insert one document
    result = clt.delete_one({'_id':data_id})
    # Check write result
    if result.acknowledged == True:
        return result.deleted_count
    else:
        return -1