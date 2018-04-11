from flask_script import Manager
from flaskbird import app
#from flaskbird.database import db

manager = Manager(app)

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


