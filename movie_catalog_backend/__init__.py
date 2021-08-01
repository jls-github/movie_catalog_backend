import os

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

from .db import db, User

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'movie-catalog-backend.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db.init_app(app)

    if test_config is None:
        # app.config.from_pyfile('config.py', silent=True)
        with app.app_context():
            # from . import routes
            db.drop_all()
            db.create_all()
    else:
        app.config.from_mapping(test_config)

    try: 
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['GET'])
    def user_records():
        """Create a user via query string parameters."""
        username = request.args.get('user')
        email = request.args.get('email')
        print(email)
        if username and email:
            new_user = User(
                username=username,
                email=email
            )
            db.session.add(new_user)  # Adds new User record to database
            db.session.commit()  # Commits all changes
        return make_response(jsonify(users=[i.serialize for i in User.query.all()])
)

    return app

