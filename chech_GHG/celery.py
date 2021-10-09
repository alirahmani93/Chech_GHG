import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chech_GHG.settings')

app = Celery('chech_GHG')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()