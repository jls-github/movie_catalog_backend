from flask import current_app as app
from flask import make_response, jsonify
from flask_restful import Resource
from ..models.user import User

class UsersController(Resource):
    def get(self):
        users = User.query.all()
        return jsonify(users=[i.serialize for i in User.query.all()])
