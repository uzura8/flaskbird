from config import BaseConfig

class LocalConfig(BaseConfig):
    TESTING = False
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    IS_LOGGING_MAIL = True

    # Request params
    PARAMS_LIST_DEFAULT = {
        'per_page': 3,
        'per_page_max': 10,
    }
