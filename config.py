import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    DEBUG = False
    LOGLEVEL = "WARNING"
    LOGFILE = basedir + "/flask-template.log"
    SECRET_KEY = 'changeme-before-production'
    CSRF_ENABLED = True
    HOST = "0.0.0.0"
    PORT = 5050


class Production(Config):
    LOGFILE = "/var/log/flask-template.log"
    DEBUG = False


class Staging(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOGLEVEL = "DEBUG"


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOGLEVEL = "DEBUG"
