import os
from celery import Celery
from datetime import timedelta

# Встановлюємо модуль налаштувань Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('proj')

# Бере налаштування з Django, використовуючи префікс CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Завантажує задачі з усіх додатків Django
app.autodiscover_tasks()

# Тестова задача для перевірки роботи Celery
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Розклад для Celery Beat
app.conf.beat_schedule = {
    'send-data-every-5-seconds': {
        'task': 'myapp.tasks.send_data',
        'schedule': timedelta(seconds=5),
    },
}
