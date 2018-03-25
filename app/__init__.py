from flask import Flask
import argparse
#from flask_sqlalchemy import SQLAlchemy
#from redis import import Redis

from .views.site import site
from .views.member import member

app = Flask(
    __name__,
    instance_relative_config = True,
    static_folder='static',
    template_folder='templates')

env_choices = ['local', 'dev', 'stg', 'prod']
parser = argparse.ArgumentParser()
parser.add_argument('-e', '--env', help='Operating environment',
                    type=str, choices=env_choices,
                    default='local')
args = parser.parse_args()
env = args.env
if env not in env_choices:
    env = 'local'

app.config.from_object('config.{}.{}Config'.format(env, env.capitalize()))
app.config.from_pyfile('config.py') #from instance dir

#db = SQLAlchemy(app)
#redis = Redis()
#app.redis = redis

modules = [site, member]
for module in modules:
    app.register_blueprint(module)

