from config import BaseConfig
class LocalConfig(BaseConfig):
    # Flask
    TESTING = False
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
