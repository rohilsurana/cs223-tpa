## Objective Exam Management

### Requirements
Python 3
pip
Django==1.9.3
django-flat-theme==1.1.3
django-nested-admin==2.2.1
six==1.10.0

##### Optional
virtualenv

### Installation
 - Take time and install [python 3.x](https://docs.python.org/3.5/) and [pip](https://pip.pypa.io/en/stable/installing/)
 - As mentioned [virtualenv](https://virtualenv.pypa.io/en/latest/) is optional but recommended as it will help to keep your global environment clean.
 - Now clone this repository using `git clone https://github.com/rohilsurana/cs223-tpa.git`. In case you dont have git installed you can download the source zip from github page.
 - Now enter the following commands after replacing the directory path to which you have cloned the source
```shell
$ cd /path/to/src/
$ virtualenv venv
$ source venv/bin/activate
$ cd oem
$ pip install -r requirements.txt
# As we already have a db file in place you dont need to migrate and do all that stuff
$ python manage.py runserver
```
 - And you have the web app up and running. To test it visit `127.0.0.1:8000` or `localhost:8000`