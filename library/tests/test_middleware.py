#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : test_middleware.py
# @Time    : 2025/3/28 21:44
# @Software: PyCharm
# @function:

from django.test import TestCase, Client
from library.models import RequestLog

class MiddlewareTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_logging_middleware(self):
        """验证中间件是否记录请求（可自定义请求路径和参数）"""
        response = self.client.get("/api/books/", {"page": 2})  # 可自定义GET参数
        log = RequestLog.objects.first()
        self.assertEqual(log.path, "/api/books/")
        self.assertEqual(log.params, {"page": "2"})  # 可验证参数格式
        self.assertGreater(log.duration, 0)