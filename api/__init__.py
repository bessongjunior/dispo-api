# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Junior Bessong
"""
import json

from flask import Flask
from flask_cors import CORS
from flask_mail import Mail

# from .routes import rest_api
from .models import db
from .config import BaseConfig

#import API route // blueprint// namespace
from .utils import rest_api
from werkzeug.middleware.proxy_fix import ProxyFix



app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

app.config.from_object('api.config.BaseConfig')

mail = Mail(app)
# mail = Mail()
# mail.init_app(app) #mail instance

db.init_app(app)

rest_api.init_app(app)


CORS(app)

#blueprint instance registration
    # app.register_blueprint(admin_bp, url_prefix='/api/1.0')
    # app.register_blueprint(users_bp, url_prefix='/api/1.1')
    # app.register_blueprint(report_bp, url_prefix='/api/1.2')
#Api init instances
    # admin.init_app(app)
    # user.init_app(app)
    # report.init_app(app)

# Setup database
@app.before_first_request
def initialize_database():
    db.create_all()

"""
   Custom responses
"""

@app.after_request
def after_request(response):
    """
       Sends back a custom error with {"success", "msg"} format
    """

    if int(response.status_code) >= 204:
        response_data = json.loads(response.get_data())
        if "errors" in response_data:
            response_data = {"success": False,
                             "msg": list(response_data["errors"].items())[0][1]}
            response.set_data(json.dumps(response_data))
        response.headers.add('Content-Type', 'application/json')
    return response

