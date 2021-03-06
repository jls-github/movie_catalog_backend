import os

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

from .db import db, init_db
from .models.user import User

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'movie-catalog-backend.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    init_db(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
        with app.app_context():
            from . import routes
            db.create_all()
    else:
        app.config.from_mapping(test_config)

    try: 
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

