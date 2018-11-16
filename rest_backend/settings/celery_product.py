import os
from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_backend.settings.product')

celery_app = Celery('tasks')
celery_app.config_from_object(settings)
celery_app.autodiscover_tasks()
