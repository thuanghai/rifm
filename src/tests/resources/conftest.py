# -*- coding: utf-8 -*-
import os
import pytest

# from src.app import create_app
import sys
sys.path.append('...')
from app import create_app

@pytest.fixture
def app():
    # set os mode
    os.environ['MODE'] = 'TESTING'
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()