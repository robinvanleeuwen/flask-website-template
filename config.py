import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    DEBUG = True
    SECRET_KEY = 'changeme-before-production'
    CSRF_ENABLED = True
    LOGLEVEL = "WARNING"
    LOGFILE = basedir + "/flask-template.log"


class Production(Config):
    DEBUG = False


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOGLEVEL = "DEBUG"
