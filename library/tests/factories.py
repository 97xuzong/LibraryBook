#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : factories.py
# @Time    : 2025/3/28 22:28
# @Software: PyCharm
# @function:

# library/tests/factories.py
import factory
from library.models import Book
from django.contrib.auth.models import User
from django.utils import timezone


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=4)
    author = factory.Faker("name")
    isbn = factory.Faker("isbn13")
    published_date = factory.Faker("date_this_decade")  # 自动生成日期
    quantity = factory.Faker("random_int", min=1, max=10)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.Faker("password")
