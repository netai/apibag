from flask import Flask
from flask import Blueprint
from .routes import web_routes
from .environment import env

web_blueprint = Blueprint('app', __name__, template_folder='templates', static_folder='static', url_prefix='/')
web_routes(web_blueprint)

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(env[env_name])
    return app
