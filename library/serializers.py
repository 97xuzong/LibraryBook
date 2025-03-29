#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : serializers.py
# @Time    : 2025/3/27 18:16
# @Software: PyCharm
# @function:


from rest_framework import serializers
from .models import Book, BorrowRecord


# 定义序列化器
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = '__all__'
        read_only_fields = ('borrow_date', 'due_date', 'return_date')
