# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
'app.py'

App boot is handled by this module (app.py)

Copyright (c) 2016-2023 EncoreSky Ltd. All rights reserved.
"""

import os
from flask import Flask
from flask_boilerplate.app.conf.config import DevelopmentConfig
from flask_boilerplate.app.routes.endpoints import demo

# Registering app and config.
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Registering url routes for similarity calculation.
app.register_blueprint(demo, url_prefix='/')

from flask_boilerplate.exceptions.error_handler import *

# Running app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ["APP_PORT"], debug=True)