import os
import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_login import LoginManager
from flaskbird.database import init_db

from .views.site import site
from .views.member import member

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

    init_db(app)
    return app

app = create_app()
login = LoginManager(app)

import flaskbird.models
from flaskbird.models import Member
from .views import error

@login.user_loader
def load_member(id):
    return Member.query.get(int(id))

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
