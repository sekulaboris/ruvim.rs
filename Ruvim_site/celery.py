import os
from celery import shared_task  
from celery import Celery






#-------------------------------- celery----------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Ruvim_site.settings')
app=Celery ('Ruvim_site')
app.config_from_object ('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


