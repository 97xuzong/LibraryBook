# library/tests/test_apis.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from library.models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="apitester", password="12345")
        self.client.force_authenticate(user=self.user)

    def test_create_book_with_required_fields(self):
        """验证创建新书时必须提供所有非空字段"""
        url = reverse("book-list")
        data = {
            "title": "New Book",
            "author": "Author X",
            "isbn": "9780981467382",
            "published_date": "2024-01-01",  # ✅ 包含 published_date
            "quantity": 10
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)

    def test_create_book_missing_published_date(self):
        """验证缺少 published_date 时返回错误"""
        url = reverse("book-list")
        data = {
            "title": "Invalid Book",
            "author": "Author Y",
            "isbn": "9780981467399",
            "quantity": 5
            # ❌ 缺少 published_date
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("published_date", response.data)  # 检查错误提示