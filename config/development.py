# -*- coding: utf-8 -*-
from .default import Config

class DevelopmentConfig(Config):
    DEBUG = True
    # RIFM(Restful Interface For MongoDB) Server IP or DNS Name
    HOST = '0.0.0.0'
    # RIFM(Restful Interface For MongoDB) Server Port
    PORT = 8000
    # MongoDB Host
    MONGO_HOST = '0.0.0.0'
    # MongoDB Port
    MONGO_PORT = 27017