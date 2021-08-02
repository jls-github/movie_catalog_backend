from flask import current_app as app
from flask_restful import Api

from .controllers.user import UsersController

api = Api(app)

api.add_resource(UsersController, '/users')
