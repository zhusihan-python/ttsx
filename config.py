import os
#get file path
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'python_zhu'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[TTSX]'
    FLASKY_MAIL_SENDER = 'TTSX Admin <jtsh12@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    MIAL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or\
        "sqlite:///" + os.path.join(basedir, "data.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config = {
    'development': DevConfig,
    'production': ProdConfig,

    'default': DevConfig
}