# FastAPI CRUD Demo

A simple CRUD (Create, Read, Update, Delete) application built with FastAPI and SQLAlchemy.

## Features

- Create new items
- Read all items or a single item by ID
- Update existing items
- Delete items
- Automatic API documentation (Swagger UI)

## Requirements

- Python 3.12+
- uv (Python package manager)

## Installation

1. **Install dependencies:**
   ```bash
   uv install
   ```

2. **Project Structure**

```
fastapi/
├── main.py                 # 应用入口
├── app/
│   ├── __init__.py        # 包初始化和数据库表创建
│   ├── database.py        # 数据库配置
│   ├── models.py          # SQLAlchemy数据模型
│   ├── schemas.py         # Pydantic验证模型
│   ├── crud.py            # CRUD操作实现
│   └── routes.py          # API路由定义
├── README.md              # 项目说明文档
└── pyproject.toml         # 项目配置和依赖
```

## Usage

1. **Run the application:**
   ```bash
   uv run main.py
   ```

2. **Access the API documentation:**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Endpoints

- **GET /**: Welcome message
- **POST /api/items/**: Create a new item
- **GET /api/items/**: Get all items
- **GET /api/items/{item_id}**: Get a specific item by ID
- **PUT /api/items/{item_id}**: Update an existing item
- **DELETE /api/items/{item_id}**: Delete an item

## Example Requests

### Create an Item
```bash
curl -X 'POST' \
  'http://localhost:8000/api/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Test Item", "description": "A test item", "price": 19.99}'
```

### Get All Items
```bash
curl -X 'GET' \
  'http://localhost:8000/api/items/' \
  -H 'accept: application/json'
```

### Get Item by ID
```bash
curl -X 'GET' \
  'http://localhost:8000/api/items/1' \
  -H 'accept: application/json'
```

### Update Item
```bash
curl -X 'PUT' \
  'http://localhost:8000/api/items/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Updated Item", "description": "An updated item", "price": 24.99}'
```

### Delete Item
```bash
curl -X 'DELETE' \
  'http://localhost:8000/api/items/1' \
  -H 'accept: application/json'
```