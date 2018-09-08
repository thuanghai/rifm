# -*- coding: utf-8 -*-
import os
import pytest

# from src.app import create_app
import sys
sys.path.append('...')
from config import load_config
from common import database
from app import create_app

@pytest.fixture
def app():
    # set os mode
    os.environ['MODE'] = 'TESTING'
    cfg = load_config()
    # set app for test
    app = create_app(cfg)
    # initialize mongodb
    database.mongo.init_app(app, cfg.MONGO_URI) 

    yield app
    # close mongodb to clean up resource
    database.mongo.cx.close()


@pytest.fixture
def client(app):
    return app.test_client()