import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jokes.settings')

app = Celery('Jokes')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_joke_3s':{
        'task': 'web.tasks.get_joke',
        'schedule': 3.0
    }
}

app.autodiscover_tasks()