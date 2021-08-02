from flask import current_app as app
from flask import request, jsonify
from flask_restful import Resource, reqparse
from ..models.user import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')

class UsersController(Resource):
    def get(self):
        users = User.query.all()
        return jsonify(users=[i.serialize for i in User.query.all()])

    def post(self):
        args = parser.parse_args()
        user = User.create(username=args['username'], email=args['email'])
        return jsonify(user.serialize)

