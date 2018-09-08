# -*- coding: utf-8 -*-
from .default import Config

class ProductionConfig(Config):
    DEBUG = False
    # RIFM(Restful Interface For MongoDB) Server IP or DNS Name
    HOST = '0.0.0.0'
    # RIFM(Restful Interface For MongoDB) Server Port
    PORT = 27080
    # MongoDB Host
    MONGO_HOST = '0.0.0.0'
    # MongoDB Port
    MONGO_PORT = 27017
    # DB Name
    MONGO_DB_NAME = 'xxx'