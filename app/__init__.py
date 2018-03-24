from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
#from redis import import Redis

from .views.site import site
from .views.member import member

app = Flask(
    __name__,
    instance_relative_config = True,
    static_folder='static',
    template_folder='templates')

app.config.from_object('config')
app.config.from_pyfile('config.py') #from instance dir

#db = SQLAlchemy(app)
#redis = Redis()
#app.redis = redis

modules = [site, member]
for module in modules:
    app.register_blueprint(module)

