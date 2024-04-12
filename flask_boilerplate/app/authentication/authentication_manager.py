# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
'authentication_manager.py'

Authentication managed by the module (app.authentication.authentication_manager)

Copyright (c) 2016-2023 EncoreSky Ltd. All rights reserved.
"""

import os
import base64
from functools import wraps
from dotenv import load_dotenv
from flask import request, jsonify
from cryptography.fernet import Fernet
from flask_boilerplate.app.conf.config import DevelopmentConfig

load_dotenv()
fernet = Fernet(DevelopmentConfig.FERNET_KEY)

def authenticate_credentials(dec_username, dec_password):
    enc_username = os.environ["AUTHENTICATION_USERNAME"]
    enc_password = os.environ["AUTHENTICATION_PASSWORD"]

    bytes_user = bytes(enc_username, 'utf-8')
    bytes_pass = bytes(enc_password, 'utf-8')

    dec_user = fernet.decrypt(bytes_user).decode()
    dec_pass = fernet.decrypt(bytes_pass).decode()

    if (dec_username == dec_user
        and dec_password == dec_pass):
        return True

    return False

def decode_credentials(auth_creds):
    #Decode Credentials
    enc_creds = auth_creds.encode("ascii")
    enc_creds = base64.b64decode(enc_creds)
    dec_creds = enc_creds.decode("ascii")
    dec_creds = dec_creds.split(":")
    dec_username, dec_password = dec_creds[0], dec_creds[1]

    return dec_username, dec_password

def authentication_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        if not 'Authorization' in request.headers:
            return jsonify({'message' : "Missing authorization header"}), 401

        auth_creds = request.headers["Authorization"].split("Basic ")[1]

        try:
            dec_username, dec_password = decode_credentials(auth_creds)
        except:
            return jsonify({'message' : "Authentication Failed"}), 401

        if not authenticate_credentials(dec_username, dec_password):
            return jsonify({'message' : "Credentials are invalid"}), 401

        return  f(*args, **kwargs)
  
    return decorated
