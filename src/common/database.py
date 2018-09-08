# -*- coding: utf-8 -*-
from flask_pymongo import PyMongo

mongo = PyMongo()

# class MongoOperator:
#     def __init__(self, flask_app, uri):
#         self.mongo = PyMongo(flask_app, uri)

# def init_db(flask_app, uri):
#     global mongo
#     mongo = PyMongo(flask_app, uri)

# from pymongo import MongoClient
# from bson.objectid import ObjectId

# def db_connect(
#     # mongo_cfg: dict(type=tuple, help='MongoDB host and port'),
#     db_host: dict(type=str, help='MongoDB database host'),
#     db_port: dict(type=str, help='MongoDB database port'),
#     db_name: dict(type=str, help='MongoDB database name')
# ):
#     """
#     Connect mongodb servery
#     """
#     # Make a connection with 'MongoClient'
#     client =  MongoClient(db_host, db_port)
#     # Get database with name 'db_name'
#     db = client[db_name]
#     return db

# def db_close(client):
#     """
#     Close mongodb
#     """
#     # type of client is pymongo.database
#     client.close()

# def create_one(
#     db_host: dict(type=str, help='MongoDB database host'),
#     db_port: dict(type=str, help='MongoDB database port'),
#     db_name: dict(type=str, help='MongoDB database name'), 
#     collection_name: dict(type=str, help ='MongoDB collection name'), 
#     data
# ):
#     """
#     Insert one document of mongodb
#     """
#     # Get database
#     db = db_connect(db_host, db_port, db_name)
#     # Get collection
#     clt = db[collection_name]
#     # Insert one document
#     result = clt.insert_one(data)
#     # Check write result
#     if result.acknowledged == True:
#         return result.inserted_id
#     else:
#         return ''
def create_one(
    collection: dict(type = str, help = 'MongoDB Collection Name'),
    data: dict(type = dict, help = 'Insert Data')
):
    """
    Insert one document of mongodb
    """
    result = {
        'l1_signal_element': lambda data: mongo.db.l1_signal_element.insert_one(data),
        'l2_control_frame': lambda data: mongo.db.l2_control_frame.insert_one(data),
        'l2_ip_data': lambda data: mongo.db.l2_ip_data.insert_one(data),
        'l3_email': lambda data: mongo.db.l3_email.insert_one(data),
        'l3_http': lambda data: mongo.db.l3_http.insert_one(data)
    }[collection](data)
    if result.acknowledged == True:
        return result.inserted_id
    else:
        return ''

# def find_one(
#     db_host: dict(type=str, help='MongoDB database host'),
#     db_port: dict(type=str, help='MongoDB database port'),
#     db_name: dict(type=str, help='MongoDB database name'), 
#     collection_name: dict(type=str, help='MongoDB collection name'), 
#     data_id: dict(type=str, help='MongoDB document id')
# ):
#     """
#     Find one document by its '_id'
#     """
#     # Get database
#     db = db_connect(db_host, db_port, db_name)
#     # Get collection
#     clt = db[collection_name]
#     # Find document by 'id'
#     return clt.find_one({'_id': data_id})
def find_one(
    collection: dict(type = str, help = 'MongoDB Collection Name'),
    id: dict(type = str, help = "MongoDB Document '_id'")
):
    """
    Find one document by its '_id'
    """
    result = {
        'l1_signal_element': lambda id: mongo.db.l1_signal_element.find_one({'_id': id}),
        'l2_control_frame': lambda id: mongo.db.l2_control_frame.find_one({'_id': id}),
        'l2_ip_data': lambda id: mongo.db.l2_ip_data.find_one({'_id': id}),
        'l3_email': lambda id: mongo.db.l3_email.find_one({'_id': id}),
        'l3_http': lambda id: mongo.db.l3_http.find_one({'_id': id})
    }[collection](id)
    return result

# def update_one(
#     db_host: dict(type=str, help='MongoDB database host'),
#     db_port: dict(type=str, help='MongoDB database port'),
#     db_name: dict(type=str, help='MongoDB database name'), 
#     collection_name: dict(type=str, help='MongoDB collection name'), 
#     data: dict(type=str, help='String for JSON data expression'),
#     data_id: dict(type=str, help='MongoDB document id')
# ):
#     """
#     Update one document field
#     """
#     # Get database
#     db = db_connect(db_host, db_port, db_name)
#     # Get collection
#     clt = db[collection_name]
#     # Update and check result
#     result = clt.update_one({"_id": data_id}, data)
#     if (result.acknowledged == True) \
#         and (result.matched_count == 1) \
#         and (result.modified_count == 1):
#         return True
#     else:
#         return False
def update_one(
    collection: dict(type = str, help = 'MongoDB Collection Name'),
    id: dict(type = str, help = 'MongoDB Document ID'),
    data: dict(type = dict, help = 'Update Element Of MongoDB Document')
):
    """
    Update one document field
    """
    result = {
        'l1_signal_element': lambda id, data: mongo.db.l1_signal_element.update_one({'_id': id}, data),
        'l2_control_frame': lambda id, data: mongo.db.l2_control_frame.update_one({'_id': id}, data),
        'l2_ip_data': lambda id, data: mongo.db.l2_ip_data.update_one({'_id': id}, data),
        'l3_email': lambda id, data: mongo.db.l3_email.update_one({'_id': id}, data),
        'l3_http': lambda id, data: mongo.db.l3_http.update_one({'_id': id}, data)
    }[collection](id, data)
    if (result.acknowledged == True) \
        and (result.matched_count == 1) \
        and (result.modified_count == 1):
        return True
    else:
        return False

# def delete_one(
#     db_host: dict(type=str, help='MongoDB database host'),
#     db_port: dict(type=str, help='MongoDB database port'),
#     db_name: dict(type=str, help='MongoDB database name'), 
#     collection_name: dict(type=str, help ='MongoDB collection name'), 
#     data_id: dict(type=str, help='MongoDB document id')
# ):
#     # Get database
#     db = db_connect(db_host, db_port, db_name)
#     # Get collection
#     clt = db[collection_name]
#     # Insert one document
#     result = clt.delete_one({'_id':data_id})
#     # Check write result
#     if result.acknowledged == True:
#         return result.deleted_count
#     else:
#         return -1
def delete_one(
    collection: dict(tpye = str, help = 'MongoDB Collection Name'),
    id: dict(type = str, help = 'MongoDB Document ID')
):
    """
    Delete one document by id
    """
    result = {
        'l1_signal_element': lambda id: mongo.db.l1_signal_element.delete_one({'_id': id}),
        'l2_control_frame': lambda id: mongo.db.l2_control_frame.delete_one({'_id': id}),
        'l2_ip_data': lambda id: mongo.db.l2_ip_data.delete_one({'_id': id}),
        'l3_email': lambda id: mongo.db.l3_email.delete_one({'_id': id}),
        'l3_http': lambda id: mongo.db.l3_http.delete_one({'_id': id})
    }[collection](id)
    if result.acknowledged == True:
        return result.deleted_count
    else:
        return -1