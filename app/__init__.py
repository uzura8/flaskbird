import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
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
        static_folder='static',
        template_folder='templates')

    from instance.config import FLASKBIRD_ENV
    env = FLASKBIRD_ENV
    app.config.from_object('config.{}.{}Config'.format(env, env.capitalize()))
    app.config.from_pyfile('config.py') #from instance dir

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'member.login'
    login.login_message = _l('Please log in to access this page.')
    mail.init_app(app)
    babel.init_app(app)

    from .views.site import site
    from .views.member import member
    modules = [site, member]
    for module in modules:
        app.register_blueprint(module)

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
                toaddrs=app.config['FBD_ADMIN_MAIL'], subject='Microblog Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

    if app.config['IS_DEBUG_LOGGING']:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
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

import app.models
#from .views import error


