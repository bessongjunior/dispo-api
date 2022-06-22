# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Junior Bessong
"""
from flask import Flask
import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class BaseConfig():
 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'apidata.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "2209350117fcac11d7781fc16b11380366a134b738eb387065dadcab2ea03f38"
    JWT_SECRET_KEY = "859465a0d357621A17095af0f1c27bfc"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER') e.g:support@movie-bag.com
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')    
