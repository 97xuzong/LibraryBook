### 模型字段详细说明

以下是图书馆管理系统中各模型的字段及其含义的详细解释：

#### **注意： User用户模型默认使用Django自带的用户认证模型  

---

#### **1. `Book` 模型（图书信息）**
| 字段名            | 类型              | 说明                                                                 |
|--------------------|-------------------|----------------------------------------------------------------------|
| `title`            | `CharField`       | 书名，最大长度200字符。                                             |
| `author`           | `CharField`       | 作者，最大长度100字符。                                             |
| `isbn`             | `CharField`       | 国际标准书号（ISBN），唯一标识一本书，最大长度13字符，唯一约束。    |
| `published_date`   | `DateField`       | 图书出版日期。                                                      |
| `quantity`         | `PositiveIntegerField` | 当前库存数量，默认值为1，借书时减少，还书时增加。               |
| `created_at`       | `DateTimeField`   | 记录创建时间，首次保存时自动填充（`auto_now_add=True`）。            |
| `updated_at`       | `DateTimeField`   | 记录最后修改时间，每次保存时自动更新（`auto_now=True`）。            |

**关键约束**：
- `isbn` 唯一性确保每本书在系统中不重复。
- `quantity` 不能为负数（通过 `PositiveIntegerField` 保证）。

---

#### **2. `BorrowRecord` 模型（借阅记录）**
| 字段名            | 类型              | 说明                                                                 |
|--------------------|-------------------|----------------------------------------------------------------------|
| `user`             | `ForeignKey`      | 关联用户模型（`User`），表示借阅者。                                |
| `book`             | `ForeignKey`      | 关联图书模型（`Book`），表示被借阅的书籍。                          |
| `borrow_date`      | `DateTimeField`   | 借书时间，记录创建时自动填充（`auto_now_add=True`）。               |
| `due_date`         | `DateTimeField`   | 应还日期，默认为借书时间加30天（通过 `save` 方法自动计算）。         |
| `return_date`      | `DateTimeField`   | 实际归还日期，未归还时为 `null`。                                   |

**关键逻辑**：
- `due_date` 在保存记录时自动设置为 `borrow_date + 30天`。
- `return_date` 为空表示图书尚未归还。

---

#### **3. `RequestLog` 模型（请求日志，用于中间件）**
| 字段名            | 类型              | 说明                                                                 |
|--------------------|-------------------|----------------------------------------------------------------------|
| `path`             | `CharField`       | 请求的URL路径（如 `/api/books/`），最大长度255字符。                |
| `method`           | `CharField`       | HTTP方法（如 `GET`、`POST`），最大长度10字符。                      |
| `params`           | `JSONField`       | 请求参数（GET参数或POST数据），JSON格式存储。                       |
| `duration`         | `FloatField`      | 请求处理耗时（单位：秒），用于性能监控。                            |
| `timestamp`        | `DateTimeField`   | 请求时间戳，记录创建时自动填充（`auto_now_add=True`）。             |

**关键说明**：
- 对于POST/PUT请求，`params` 存储请求体中的JSON数据。
- 对于GET请求，`params` 存储URL中的查询参数（如 `?page=1`）。

---

### **模型关系总结**
| 模型           | 核心作用                                                                 |
|----------------|--------------------------------------------------------------------------|
| `Book`         | 管理图书的基本信息（书名、作者、库存等）。                               |
| `BorrowRecord` | 记录用户借阅行为，跟踪借书、应还日期和实际归还状态。                     |
| `RequestLog`   | 监控API请求，记录请求路径、方法、参数和耗时，用于调试和审计。            |

---

### **注意事项**
1. **数据一致性**：
   - 借书时需减少 `Book.quantity`，还书时需增加，避免库存错误。
   - 确保 `BorrowRecord` 中 `due_date` 计算逻辑正确（30天借阅期）。

2. **安全与性能**：
   - `RequestLog.params` 存储敏感数据（如密码）时需脱敏。
   - 频繁的日志写入可能影响性能，生产环境中建议异步处理。

3. **扩展性**：
   - 可添加 `Book.category` 字段分类图书。
   - 可扩展 `BorrowRecord.overdue_fee` 字段实现逾期扣费逻辑。

