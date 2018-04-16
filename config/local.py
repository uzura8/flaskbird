from config import BaseConfig

class LocalConfig(BaseConfig):
    TESTING = False
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    IS_LOGGING_MAIL = True
