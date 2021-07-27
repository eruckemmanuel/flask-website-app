from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager


app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Admin
app.config['FLASK_ADMIN_SWATCH'] = "cerulean"
admin = Admin(app, name="website")


# Authentication
http_auth = HTTPBasicAuth()

login_manager = LoginManager()
login_manager.login_view = 'auth.sign_in'
login_manager.init_app(app)

# Database
db = SQLAlchemy(app)

api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/')
def index():
    return render_template('index.html')


# Import and register app modules
from app.auth.controllers import auth

app.register_blueprint(auth)


from app.auth.models import User

admin.add_view(ModelView(User, db.session))

# REST API
from app.auth.api.users import UsersAPI

api.add_resource(UsersAPI, '/api/users')


# Build the database
db.create_all()