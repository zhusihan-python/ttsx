import sys

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from config import config

reload(sys)
sys.setdefaultencoding('utf-8')

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

