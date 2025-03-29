from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book, BorrowRecord
from .serializers import BookSerializer, BorrowRecordSerializer
from django.utils import timezone

# 接口测试时候放宽权限  不用登录可以直接测试接口
from rest_framework.permissions import AllowAny


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]  # 允许所有用户 接口功能测试用
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # 上生产使用


class BorrowReturnViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]  # 用户认证之后
    # permission_classes = [AllowAny]  # 允许所有用户 POST

    @action(detail=True, methods=['post'])
    def borrow(self, request, pk=None):
        # 校验书籍是否存在
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "查无此书"})

        # 校验是否有库存
        if book.quantity <= 0:
            return Response({"error": "书籍已经借完"}, status=status.HTTP_400_BAD_REQUEST)

        # 检查是否已有未归还记录
        existing_record = BorrowRecord.objects.filter(
            user=request.user,
            book_id=pk,
            return_date__isnull=True
        ).exists()
        if existing_record:
            return Response(
                {"error": "您已借阅该图书且尚未归还"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 校验成功之后再行租借
        book.quantity -= 1
        book.save()

        BorrowRecord.objects.create(
            user=request.user,
            book=book,
            due_date=timezone.now() + timezone.timedelta(days=8)
        )
        return Response({"status": "借书成功"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        # 校验书籍是否存在
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "归还失败 查无此书"})

        # # 校验是否有借阅
        # record = BorrowRecord.objects.filter(book=book, user=request.user, return_date__isnull=True).first()
        # if not record:
        #     return Response({"error": "未找到有效借阅记录  无需还书"}, status=status.HTTP_400_BAD_REQUEST)

        # 查看是否有借阅记录
        try:
            record = BorrowRecord.objects.get(
                book=book,
                user=request.user,
                return_date__isnull=True
            )
        except BorrowRecord.DoesNotExist:
            return Response(
                {"error": "未找到有效借阅记录"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 校验成功
        record.return_date = timezone.now()
        record.save()

        book.quantity += 1
        book.save()
        return Response({"status": "还书成功"}, status=status.HTTP_200_OK)
