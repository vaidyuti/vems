import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vems.settings.local")

app = Celery("vems")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks defined in <app>/tasks.py
app.autodiscover_tasks()
