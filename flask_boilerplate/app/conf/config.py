# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
'config.py'

App Level Configurations handled by this module (app.conf.config)

Copyright (c) 2016-2023 EncoreSky Ltd. All rights reserved.
"""

import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'URI connection'


# Configurations for app under production
class ProductionConfig(Config):
    DATABASE_URI = 'URI connection'


# Configurations for app under development
class DevelopmentConfig(Config):
    DEBUG = True
    FERNET_KEY = b'zZLhXDwI5uDzdjHlBnneEC7ZS0yPgOWgX8_3AHH9_ac='


# Configurations for app under testing.
class TestingConfig(Config):
    TESTING = True