#/bin/sh

python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py db_create_member default sample@example.com password
python manage.py generate_config_js src/js/config/site.json
