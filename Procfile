release: python manage.py clear_pgviews && python manage.py migrate && python manage.py full_ruler_update
web: gunicorn project.wsgi
