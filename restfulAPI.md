# 个人项目

Base URLs:

* <a href="http://dev-cn.your-api-server.com">http://127.0.0.1:8000/api/</a>

# 图书借阅管理API

## 1.GET 查询所有图书

GET /api/books

> 返回示例

> 200 Response

```json
[
      {
            "id": 3,
            "title": "水浒传",
            "author": "Eric Matthes",
            "isbn": "9781593279288",
            "published_date": "2019-05-01",
            "quantity": 8,
            "created_at": "2025-03-28T13:19:25.617727Z",
            "updated_at": "2025-03-29T03:34:19.403871Z"
      },
      {
            "id": 4,
            "title": "Python编程从入门到实践",
            "author": "Eric Matthes",
            "isbn": "9787115477679",
            "published_date": "2023-01-01",
            "quantity": 3,
            "created_at": "2025-03-28T15:04:59.669461Z",
            "updated_at": "2025-03-29T03:34:27.500139Z"
      }
]
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 

## 2.GET 查询单一图书

GET /api/books/6/

> 返回示例

> 200 Response

```json
{
      "id": 6,
      "title": "水浒传",
      "author": "施耐庵",
      "isbn": "9781595221",
      "published_date": "1289-05-01",
      "quantity": 99,
      "created_at": "2025-03-29T03:29:53.147293Z",
      "updated_at": "2025-03-29T05:04:44.708184Z"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 

## 3.POST 添加图书信息

POST /api/books/

params：

```json
{
            "title": "百年孤独",
            "author": "老外",
            "isbn": "12376654673",
            "published_date": "1289-05-01",
            "quantity": 100
        }
```



> 返回示例

> 200 Response

```json
{
    "id": 8,
    "title": "百年孤独",
    "author": "老外",
    "isbn": "12376654673",
    "published_date": "1289-05-01",
    "quantity": 100,
    "created_at": "2025-03-29T03:54:21.896959Z",
    "updated_at": "2025-03-29T03:54:21.896959Z"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 

## 4.PUT 修改图书信息

PUT /api/books/8

params：

```json
{
            "title": "百年孤独",
            "author": "老外11111",
            "isbn": "12376654673",
            "published_date": "1289-05-01",
            "quantity": 100
        }
```

> 返回示例

> 200 Response

```json
{
    "id": 8,
    "title": "百年孤独",
    "author": "老外11111",
    "isbn": "12376654673",
    "published_date": "1289-05-01",
    "quantity": 100,
    "created_at": "2025-03-29T03:54:21.896959Z",
    "updated_at": "2025-03-29T03:56:27.115594Z"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 

## 5.DELETE 删除图书信息

DELETE /api/books/8

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 

## 6.POST借阅图书【用户登录认证后】

POST /api/borrow/5/borrow/

> 返回示例

> 200 Response

```json
{
    "status": "借书成功"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |



## 7.POST 归还图书【用户登录认证后】

POST  /api/borrow/6/return_book/

> 返回示例

> 200 Response

```json
{
    "error": "未找到有效借阅记录"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 

