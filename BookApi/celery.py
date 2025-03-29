# library_management/celery.py

import os
from celery import Celery
from django.conf import settings

# 设置 Django 的默认环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookApi.settings')

# 创建 Celery 实例
app = Celery('BookApi')

# 从 settings.py 加载配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现所有注册的 Django app 中的 tasks.py
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# 添加调试任务
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
