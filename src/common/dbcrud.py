# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

def db_connect(
    mongo_cfg: dict(type=tuple, help='MongoDB host and port'),
    db_name: dict(type=str, help='MongoDB database name')):
    """
    Connect mongodb servery
    """
    # Make a connection with 'MongoClient'
    # 'mongo_cfg[0]' is mongodb server host
    # 'mongo_cfg[1]' is mongodb server port
    client =  MongoClient(mongo_cfg[0], mongo_cfg[1])
    # Get database with name 'db_name'
    db = client[db_name]
    return db

def create_one(
    mongo_cfg: dict(type=tuple, help='MongoDB host and port'),
    db_name: dict(type=str, help='MongoDB database name'), 
    collection_name: dict(type=str, help ='MongoDB collection name'), 
    data
):
    """
    Insert one document of mongodb
    """
    # Get database
    db = db_connect(mongo_cfg, db_name)
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
    db_name: dict(type=str, help='MongoDB database name'),
    collection_name: dict(type=str, help='MongoDB collection name'),  
    id
):
#     # # Get database
#     # db = db_connect(db_name)
#     # # Get collection
#     # clt = db[collection_name]
#     # # Find document by 'id'
#     # return clt.find_one({'_id': ObjectId(id)})
    pass

def update_one(
    mongo_cfg: dict(type=tuple, help='MongoDB host and port'),
    db_name: dict(type=str, help='MongoDB database name'), 
    collection_name: dict(type=str, help='MongoDB collection name'), 
    data: dict(type=str, help='String for JSON data expression'),
    data_id: dict(type=str, help='MongoDB document id')
):
    """
    Update one document field
    """
    # Get database
    db = db_connect(mongo_cfg, db_name)
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

def delete(
    db_name: dict(type=str, help='MongoDB database name'),
    collection_name: dict(type=str, help='MongoDB collection name'),
    id=None
):
#     # # Get database
#     # db = db_connect(db_name)
#     # # Get collection
#     # clt = db[collection_name]
#     # if id:
#     #     # Find document and delete it
#     #     return clt.delete_one({'_id': ObjectId(id)})
#     # else:
#     #     # Find all documents and delete them
#     #     return clt.delete_many({'_id': ObjectId(id)})
    pass