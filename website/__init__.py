# This file makes the website folder a python package 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# Defining a new database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # Initialize the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thekryptofleiberkun tracedaninfiniteuniversalloop' # secure the cookies and session data related to the website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #SQL Database storage location
    db.init_app(app)

    # Import and register the blueprints in this file
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    # Finding a user
    login_manager = LoginManager()
    login_manager.login_view = 'auth.index' # Where we need to go if we're not logged in
    login_manager.init_app(app) # Telling the login manager which app we're using

    # Function to load user by ID
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME): # Path module to check whether database exits
        db.create_all(app=app) # If not create database
        print('Created Database!')

    