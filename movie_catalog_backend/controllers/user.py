from flask import current_app as app
from flask import make_response, jsonify
from ..models.user import User

@app.route('/users', methods=['GET'])
def index():
    users = User.query.all()
    return make_response(jsonify(users=[i.serialize for i in User.query.all()]))
