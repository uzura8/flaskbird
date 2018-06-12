import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import importlib
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel, lazy_gettext as _l

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()
babel = Babel()

def create_app():
    app = Flask(
        __name__,
        instance_relative_config = True,
        static_folder='statics',
        template_folder='templates')

    jinja_options = app.jinja_options.copy()
    jinja_options.update({
        'block_start_string': '[%',
        'block_end_string': '%]',
        'variable_start_string': '[[',
        'variable_end_string': ']]',
        'comment_start_string': '[#',
        'comment_end_string': '#]'
    })
    app.jinja_options = jinja_options

    from instance.config import FLASKBIRD_ENV
    env = FLASKBIRD_ENV
    
    app.config.from_object('config.{}.{}Config'.format(env, env.capitalize()))
    app.config.from_pyfile('config.py') #from instance dir
    app.config['ENV'] = env

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'member.login'
    login.login_message = _l('Please log in to access this page.')
    mail.init_app(app)
    babel.init_app(app)

    app.config['FBD_MODULES'].extend(app.config['FBD_OPTIONAL_MODULES'])
    for module_name in app.config['FBD_MODULES']:
        m = importlib.import_module('app.' + module_name)
        app.register_blueprint(m.bp)

    if app.config['IS_SEND_ERROR_REPORT_MAIL']:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['FBD_ADMIN_MAIL'], subject=app.config['FBD_SITE_NAME']+' Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

    if app.config['IS_DEBUG_LOGGING']:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/mail.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Flaskbird startup')

    return app

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])

