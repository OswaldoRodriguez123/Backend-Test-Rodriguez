# Cornershop's Backend Test by Oswaldo Rodriguez

This technical test requires the design and implementation (using Django and Celery) of a management system to coordinate the meal delivery for Cornershop employees.

## INSTALLATION 

## venv
```shell
python -m venv venv
source venv/scripts/activate
```

## Project
```shell
git clone https://github.com/oswaldorodriguez123/cornershop.git
cd cornershop/
pip install -r requirements.txt
python manage.py migrate
apt-get install redis-server
```

## Add file .env
```
SECRET_KEY = "django-insecure-z#ri$h(c19u+ro(u0r$f6jw&7@ye@agbfq2v!!)vq2(x%6k435"
TOKEN_SLACK = "YOUR TOKEN SLACK"
```

## Load data in order
```shell
python manage.py loaddata menu/fixtures/users.json
python manage.py loaddata menu/fixtures/menu.json
python manage.py loaddata menu/fixtures/food.json
python manage.py loaddata menu/fixtures/option.json
python manage.py loaddata menu/fixtures/order.json
```

## Terminal 1 run django
```shell
python manage.py runserver
```

## Terminal 2 run redis
```shell
redis-server
```

## Terminal 3 run celery
```shell
celery -A cornershop.celery worker --loglevel=DEBUG
```

## Login
```
User: nora
Password:1234
```

## Menu to order
http://localhost:8000/menu/258ca5e6-75c0-4b36-a8dc-97a95e1f8c03

## To check order
http://localhost:8000/orders

## Test
python manage.py test