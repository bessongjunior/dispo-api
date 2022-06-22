# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Junior Bessong

"""


from datetime import datetime, timezone, timedelta

from functools import wraps

from flask import request #, Blueprint
from flask_restx import Api, Resource, fields, Namespace

import jwt

from api.models import db, Users, JWTTokenBlocklist
from api.config import BaseConfig

# rest_api = Api(version="1.0", title="Users API")
report = Namespace("report", description="Reports related operations")
# report_bp = Blueprint('admin', __name__) #url_prefix="/api/v1"
# report = Api(report_bp
#     #version="1.0",
#     #title="Dispo API",
#     #description="Welcome to Dispo. A site for collecting data on areas with public waste and lister!"
#     )


"""
    Flask-Restx models for api request and response data
"""

post_model = report.model('ReportModel', {"gpslocation": fields.String(required=True, min_length=2, max_length=32),
                                              "city": fields.String(required=True, min_length=4, max_length=64),
                                              "mlresult": fields.String(required=True, min_length=4, max_length=16),
                                              "date_posted": fields.String(required=True, min_length=4, max_length=64),
                                              "user_id": fields.String(required=True, min_length=4, max_length=64)
                                              })
  

"""
    Flask-Restx routes
"""


@report.route('/api/report/post')
class Post(Resource):
    """
       Creates a new user by taking 'post_model' input
    """

    @report.expect(post_model, validate=True)
    def post(self):

        req_data = request.get_json()

        _gpslocation = req_data.get("gpslocation")
        _city = req_data.get("city")
        _mlresult = req_data.get("mlresult")
        _date_posted = req_data.get(datetime.now(timezone.utc))
        _user_id = req_data.get("user_id")


        new_post = ImageGPSData(gpslocation=_gpslocation, city=_city, mlresult=_mlresult, date_posted=_date_posted, user_id=_user_id)

        # new_post.set_pictuer(_picture)
        new_user.save()

        return {"success": True,
                "userID": new_user.id,
                "msg": "The report post was successfully registered"}, 200
