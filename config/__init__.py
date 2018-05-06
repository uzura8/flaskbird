class BaseConfig(object):
    FLASKBIRD_VERSION = '0.1.0Alpha'
    FLASKBIRD_ENV = 'local'

    # instance
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None

    # Flask
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    # Babel
    LANGUAGES = ['en', 'ja']

    FBD_ADMIN_MAIL = 'admin@example.com'

    # Flaskbird
    IS_DEBUG_LOGGING = False
    IS_SEND_ERROR_REPORT_MAIL = False
    # Modules
    FBD_MODULES = ['error', 'site', 'member', 'api']
    FBD_OPTIONAL_MODULES = []
    # Mail
    MAIL_SERVER = None
    MAIL_PORT = 25
    MAIL_USE_TLS = None
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    ADMINS = None
    IS_LOGGING_MAIL = False

