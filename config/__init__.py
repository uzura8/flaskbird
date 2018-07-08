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

    # Flaskbird
    FBD_SITE_NAME = 'FlaskBird'
    FBD_ADMIN_MAIL = 'admin@example.com'
    IS_DEBUG_LOGGING = False
    IS_SEND_ERROR_REPORT_MAIL = False
    # Modules
    FBD_MODULES = ['error', 'site', 'media', 'member', 'api']
    FBD_OPTIONAL_MODULES = []
    # Mail
    MAIL_SERVER = None
    MAIL_PORT = 25
    MAIL_USE_TLS = None
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    ADMINS = None
    IS_LOGGING_MAIL = False

    # Request params
    PARAMS_LIST_DEFAULT = {
        'per_page': 10,
        'per_page_max': 100,
    }

    # Upload
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024
    MEDIA_DIR_NAME = 'media'
    UPLOAD_SPLIT_DIRS_COUNT = 10
    UPLOAD_ALLOWED_MEDIA = {
        'photo':{
            'types':{
                'jpeg':'image/jpeg',
                'jpg':'image/jpeg',
                'png':'image/png',
                'gif':'image/gif',
            },
            'sizes':['200x200xc', '600x600'],
        }
    }

