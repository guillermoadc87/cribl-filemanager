import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from .api.v1 import v1_blueprint
from logging.config import dictConfig
from config import config as app_config

def create_app(config=None):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=2, x_host=1)

    # name of the configuration class if the value is of string type
    config_name = config
    if not isinstance(config, str):
        # default configuration class name
        config_name = os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(app_config[config_name])
    dictConfig(app.config["LOGGIN"])

    app.register_blueprint(v1_blueprint)

    return app
