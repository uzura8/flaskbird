class BaseConfig(object):
    FLASKBIRD_ENV = 'local'

    # instance
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None
    #REDIS_URL = None

    # Flask
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
