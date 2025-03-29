# library/middleware.py
import json
import time
from django.utils.deprecation import MiddlewareMixin
from .models import RequestLog


class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 接受请求前处理
        request.start_time = time.time()
        # 缓存请求体内容
        if request.method in ['POST', 'PUT', 'PATCH']:
            request._body_cache = request.body  # 保存原始字节流

    def process_response(self, request, response):
        # 响应发送前处理
        duration = time.time() - request.start_time
        params = {}

        # 处理 GET 请求参数
        if request.method == 'GET':
            params = request.GET.dict()

        # 处理 POST/PUT/PATCH 请求参数  兼容多种入参格式
        elif request.method in ['POST', 'PUT', 'PATCH']:
            content_type = request.content_type.lower()

            # 使用缓存的请求体
            body = getattr(request, '_body_cache', b'')

            # 表单数据（如 multipart/form-data）
            if content_type in ['application/x-www-form-urlencoded', 'multipart/form-data']:
                params = request.POST.dict()

            # JSON 数据
            elif content_type == 'application/json':
                try:
                    params = json.loads(body.decode('utf-8'))  # 从缓存解析 JSON
                except json.JSONDecodeError:
                    params = {'error': 'Invalid JSON'}

            # 其他格式（如 XML）
            else:
                params = {'error': f'Unsupported content type: {content_type}'}

        # 创建日志记录
        RequestLog.objects.create(
            path=request.path,
            method=request.method,
            params=params,
            duration=duration
        )
        return response
