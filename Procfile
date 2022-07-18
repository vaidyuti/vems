release: python manage.py migrate
web: gunicorn -w 2 --log-file=- -b :$PORT vems.wsgi:application
