"""WSGI config for school_application project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_application.settings')

application = get_wsgi_application()
