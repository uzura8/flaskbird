from flask import Flask
from flask_login import LoginManager
from flaskbird.database import init_db
import flaskbird.models
from flaskbird.models import Member

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

from .views import error

@login.user_loader
def load_member(id):
    return Member.query.get(int(id))

modules = [site, member]
for module in modules:
    app.register_blueprint(module)

