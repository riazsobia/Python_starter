# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
'controller.py'

Controllers of endpoints handled by this module (app.controllers.controller)

Copyright (c) 2016-2023 EncoreSky Ltd. All rights reserved.
"""

from flask import request
from flask_boilerplate.core.operations.addition import addition
from flask_boilerplate.app.authentication.authentication_manager import authentication_required


@authentication_required
def add_numbers():
    # try:
        inputs = request.get_json()
        
        value_1 = inputs.get("value_1")
        value_2 = inputs.get("value_2")

        return {
            "sum": addition(value_1=value_1, value_2=value_2)
        }, 200

    # except Exception as e:
    #     return {
    #         "message": str(e)
    #     }, 404
