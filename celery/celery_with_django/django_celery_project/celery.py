from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Seoul')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    # periodic task Name
    'send-mail-every-day-at-8': {
        # 실행할 업무 appname.task file name.함수명
        'task': 'mainapp.tasks.test_func',
        # 크론탭 설정
        # https://lucky516.tistory.com/18
        'schedule': crontab(),
        # 'schedule': crontab(hour=11, minute=16),
        # 'schedule': crontab(hour=0, minute=1, day_of_month=19, month_of_year=6),
        # 'args': (2,)
    }
}

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')