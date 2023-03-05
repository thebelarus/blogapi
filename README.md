# Blog Api
### Simple blog-api using Django Rest Framework

#### make .env
```bash
DEBUG=False
SECRET_KEY='secret_key_string'
DATABASE_URL='sqlite:///db.sqlite3'
```
#### configure
```python
pip install -r requirements.txt
python manage.py collectstatic
python manage.py migrate
python manage.py createsuperuser
```
### run project
For dev
```python
python manage.py runserver
```
For prod
```python
gunicorn django_project.wsgi
```
