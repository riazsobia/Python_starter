# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
'endpoints.py'

All Endpoints app are defined in this module (app.routes.endpoints.py)

Copyright (c) 2016-2023 EncoreSky Ltd. All rights reserved.
"""

from flask import Blueprint
from flask_boilerplate.app.controllers.controller import add_numbers

# Creating blueprint for similarity urls.
demo = Blueprint('demo', __name__)

# Defining url routes for similarity calculation.
demo.route('/addition', methods=['POST'])(add_numbers)