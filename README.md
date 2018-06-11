Installation
============

### 1. Install required libraries ###

~~~~
pip install -r requirements.txt
~~~~

### 2. Create DB ###

~~~~
echo "CREATE DATABASE DB-name DEFAULT CHARACTER SET utf8" | mysql -u root -p
~~~~

### 3. Set config file and edit for each environment ###

~~~~
$ cp instance/config.py.sample instance/config.py
$ vi instance/config.py
~~~~

### 4. Setup ###

~~~~
sh bin/setup.sh
~~~~

And you can login at default user: default / password
