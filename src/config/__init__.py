# -*- coding: utf-8 -*-

import os

def load_config():
    """
    Get different configuration with your setting in app.py
    """
    mode = os.environ.get('MODE')

    if mode == 'DEVELOPMENT':
        from .development import DevelopmentConfig
        return DevelopmentConfig
    elif mode == 'PRODUCTION':
        from .production import ProductionConfig
        return ProductionConfig
    elif mode == 'TESTING':
        from .testing import TestingConfig
        return TestingConfig
    else:
        from .default import Config
        return Config