"""Default ASGI config for school_application project."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_application.settings')

application = get_asgi_application()
