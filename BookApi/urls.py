"""BookApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import BookViewSet, BorrowReturnViewSet

# 使用drf框架特性注册路由
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'borrow', BorrowReturnViewSet, basename='borrow')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

'''
API接口信息:
book- curd  
    /api/books/...
借书还书
    /api/borrow/<pk>/borrow/
    /api/borrow/<pk>/return_book/

'''
