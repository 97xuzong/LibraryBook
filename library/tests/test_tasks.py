# tests/test_tasks.py
from django.test import TestCase
from django.utils import timezone
from library.models import Book, User, BorrowRecord
from library.tasks import send_due_date_reminders
from unittest.mock import patch

from library.tests.factories import UserFactory, BookFactory


class CeleryTaskTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        # self.book = BookFactory()  # 自动填充所有字段，包括 published_date
        self.book = Book.objects.create(
            title="Django for Professionals",
            author="William S. Vincent",
            isbn="9780981467368",
            published_date="2023-01-01",  # 必填字段
            quantity=5
        )
        self.record = BorrowRecord.objects.create(
            user=self.user,
            book=self.book,
            due_date=timezone.now() + timezone.timedelta(days=3)
        )

    @patch("django.core.mail.send_mail")
    def test_send_due_reminders(self, mock_send_mail):
        send_due_date_reminders.delay()
        mock_send_mail.assert_called_once_with(
            "Book Return Reminder",
            f"Your book {self.book.title} is due on {self.record.due_date}. Please return it soon.",
            "library@example.com",
            [self.user.email]
        )