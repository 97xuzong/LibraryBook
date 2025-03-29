#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : tasks.py
# @Time    : 2025/3/27 18:23
# @Software: PyCharm
# @function:

from celery import shared_task
from django.utils import timezone
from .models import BorrowRecord
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_due_date_reminders():
    # 七天内到期的借书记录
    seven_days_later = timezone.now() + timezone.timedelta(days=7)
    records = BorrowRecord.objects.filter(
        due_date__lte=seven_days_later,
        return_date__isnull=True
    )
    for record in records:
        send_mail(
            subject='借书归还提醒',
            message=f'你的书籍 {record.book.title} 到期时间为 {record.due_date}. 请及时归还',
            from_email=settings.EMAIL_FROM,
            recipient_list=[record.user.email],
            fail_silently=False,
        )
