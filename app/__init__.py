# from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

#bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    
    # creating the app configuration
    app.config.from_object(config_options[config_name])
    
    # Initializing flask extension
    bootstrap.init_app(app)     

    # Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .requests import configure_request
    configure_request(app)

    return app

