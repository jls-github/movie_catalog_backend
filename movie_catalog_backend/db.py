import click
from flask import current_app
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models.user import User
from .models.movie import Movie

@click.command('drop-db')
@with_appcontext
def drop_db_command():
    db.drop_all()
    click.echo('Dropped the database')

@click.command('create-db')
@with_appcontext
def create_db_tables_command():
    db.create_all()
    click.echo('Created tables in the database')

def add_cli_commands(app):
    app.cli.add_command(drop_db_command)
    app.cli.add_command(create_db_tables_command)

def init_db(app):
    db.init_app(app)
    add_cli_commands(app)

