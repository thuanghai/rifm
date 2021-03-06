# -*- coding: utf-8 -*-
class Config(object):
    DEBUG = True
    # RIFM(Restful Interface For MongoDB) Server IP or DNS Name
    HOST = '0.0.0.0'
    # RIFM(Restful Interface For MongoDB) Server Port
    PORT = 27080
    # MongoDB Host
    MONGO_HOST = '0.0.0.0'
    # MongoDB Port
    MONGO_PORT = 27017
    # DB Name
    MONGO_DB_NAME = 'dev'
    # MONGODB URI
    MONGO_URI = 'mongodb://' + MONGO_HOST + ':' + str(MONGO_PORT) + '/' + MONGO_DB_NAME