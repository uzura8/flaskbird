from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def db_create():
    ''' Setup db '''
    db.create_all()
    print('db created.')

@manager.command
def db_create_member(name, email, password):
    '''Create member'''
    from app.member.models import Member
    member = Member(name=name, email=email, password=password)
    member.set_password(password)
    db.session.add(member)
    db.session.commit()
    print('Create member' + name)

@manager.command
def convert_translate_json (input_file, output_dir):
    from app.common.vuei18n_jsonformatter import VueI18nJsonFormatter
    '''Convert json file created by pojson to vue-i18n format'''
    formatter = VueI18nJsonFormatter(input_file, output_dir);
    formatter.execute()

@manager.command
def generate_translate_json_en (input_file, output_dir):
    from app.common.vuei18n_jsonformatter import VueI18nJsonFormatter
    '''Generate en json file from pojson of other lang'''
    formatter = VueI18nJsonFormatter(input_file, output_dir,
                                        {'init_en':True})
    formatter.execute()

@manager.command
def generate_config_js (output_dir):
    from app.common.site.util import config_js
    from app.common.file import put_json_from_dict
    '''Generate config json file from flask config'''
    put_json_from_dict(output_dir, config_js())

@manager.option('-b', '--bird', help='Target bird')
def bird(bird=''):
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
    if bird:
        sound = sounds[bird]
    else:
        import random
        bird, sound = random.choice(list(sounds.items()))
    print('{} sings "{}"'.format(bird, sound))


if __name__ == '__main__':
    manager.run()


