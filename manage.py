from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskbird import app
from flaskbird.database import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def db_create():
    ''' Setup db '''
    db.create_all()
    print('db created.')

@manager.command
def bird():
    import random
    ''' Some birds sing '''
    sounds = {
        'duck': 'quack',
        'rooster': 'cock-a-doodle-doo',
        'cuckoo': 'cuckoo',
        'crow': 'caw',
        'dove': 'coo',
        'chick': 'cheep',
        'owl': 'hoot',
    }
    bird, sound = random.choice(list(sounds.items()))
    print('{} sings "{}"'.format(bird, sound))


if __name__ == '__main__':
    manager.run()

