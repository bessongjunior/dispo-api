from flask_restx import Api

from api.admin.routes import admin as admin_api
from api.user.routes import user as user_api
from api.report.routes import report as report_api

rest_api = Api(title="Dispo API", version="1.1", description="Version 1.0 of Dispo API for Multi User Authentication.",)

rest_api.add_namespace(admin_api)
rest_api.add_namespace(user_api)
rest_api.add_namespace(report_api)