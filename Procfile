web: python manage.py migrate && gunicorn magicstore.wsgi
web2: daphne magicstore.asgi:application --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2