# library/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from library.models import Book, BorrowRecord
from .factories import BookFactory,UserFactory


class BookModelTests(TestCase):
    def setUp(self):
        self.book = BookFactory()  # 自动填充所有字段

    def test_book_creation(self):
        self.assertIsNotNone(self.book.published_date)


class BorrowRecordModelTests(TestCase):
    def setUp(self):
        # 提供所有非空字段的值
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            isbn="1234567890123",
            published_date="2023-01-01"
        )

    def test_borrow_record_creation(self):
        """验证借阅记录的必填字段"""
        record = BorrowRecord.objects.create(user=self.user, book=self.book)
        self.assertIsNotNone(record.due_date)