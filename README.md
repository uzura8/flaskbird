Installation
============

### 1. Set config file and edit for each environment ###

~~~~
$ cp instance/config.py.sample instance/config.py
$ vi instance/config.py
~~~~

### 2. Setup db ###

~~~~
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
~~~~
