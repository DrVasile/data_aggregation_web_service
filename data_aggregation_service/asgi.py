"""
ASGI config for data_aggregation_service project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_aggregation_service.settings')

application = get_asgi_application()
