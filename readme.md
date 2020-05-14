# darenda project ![](https://img.shields.io/badge/python-3.7-blue.svg)
# GETTING STARTED
**IMPORTANT:** All packages listed in `pip-requirements.txt`.
## INSTALL
* Install python version 3.7 or later [HERE](https://www.python.org/downloads/)
* Create an [VIRTUAL ENV](https://docs.python.org/3/library/venv.html)
```bash
$ py -m venv `name YOUR virtual environmental`
```
* Activate VENV
```bash
$ cd  /path/to/new/virtual/environment
$ source Scripts/activate
$ pip install -r requirements.txt
```
* Run application
```bash
$ cd  darenta/cms
$ python manage.py migrate
$ python manage.py runserver
```
**ADMIN Panel:**
* http://127.0.0.1:8000/admin/
* superusername: admin
* superuserpassword: admin