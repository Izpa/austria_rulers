# Austria rulers



## Requirements
Python 3.6

Django 2.0.1

## Download

https://github.com/Izpa/austria_rulers/archive/develop.zip

or

```
git@github.com:Izpa/austria_rulers.git
```

## Installation
In virtualenv run

```
pip install -r requirements.txt
```

Then you cat set environment variable

```
export LOCATION="production"
export SECRET_KEY="some random string"
export DATABASE_URL="sdfff"
```

By default LOCATION set as 'local', database on localhost, on port 5432, with user postgres, password postgres,
and austria_rulers database

Collect static files, do database migrations, update austria rulers from wikipedia and create superuser for admin page

```
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py full_ruler_update
python manage.py createsuperuser
```


And then run the web-application

```
python manage.py runserver
```

Now web-application running on http://127.0.0.1:8000/

Also you can use docker-compose

```
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py createsuperuser
```