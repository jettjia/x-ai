# Python Project Template

一个标准的Python项目模板，演示了如何按照最佳实践创建和组织Python项目。

## 项目特点

- 符合PEP 8标准的代码规范
- 完整的目录结构
- 支持虚拟环境
- 包含单元测试
- 支持打包和发布
- 详细的文档说明

## 项目结构

```
project_template/
├── src/
│   └── project_template/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── data/
├── docs/
├── setup.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 安装说明

### 1. 克隆项目（示例）

```bash
# 克隆项目到本地
git clone <repository-url>
cd project_template
```

### 2. 创建虚拟环境

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
# 激活虚拟环境
# macOS/Linux
source venv/bin/activate
# Windows
# venv\Scripts\activate
```

### 3. 安装项目依赖

```bash
# 安装基本依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -e "[dev]"
```

### 4. 以开发模式安装项目

```bash
pip install -e .
```

## 使用方法

### 作为模块导入

```python
from project_template import hello_world

# 调用函数
message = hello_world()
print(message)  # 输出: Hello, World!
```

### 命令行工具

安装项目后，可以直接使用命令行工具：

```bash
project_template
# 输出: Hello, World!
```

## 项目功能

### 1. 创建项目结构

该项目提供了一个函数，可以帮助快速创建标准的Python项目结构：

```python
from project_template import create_project_structure

# 创建新的项目结构
new_project_path = create_project_structure("my_new_project")
print(f"项目已创建在: {new_project_path}")
```

## 运行测试

```bash
# 使用unittest运行测试
python -m unittest discover tests

# 或者使用pytest（如果已安装）
pytest
```

## 开发指南

### 代码风格

请确保代码符合PEP 8标准：

```bash
# 检查代码风格
flake8 src/
```

### 添加新功能

1. 在`src/project_template/`目录下创建新的模块文件
2. 在`__init__.py`中导入并导出新功能
3. 为新功能编写测试用例
4. 更新README.md文档

## 打包和发布

### 生成requirements.txt

```bash
pip freeze > requirements.txt
```

### 构建项目

```bash
python setup.py sdist bdist_wheel
```

### 安装构建的包

```bash
pip install dist/project_template-0.1.0.tar.gz
# 或者
pip install dist/project_template-0.1.0-py3-none-any.whl
```

## 虚拟环境管理

### 创建虚拟环境

```bash
python3 -m venv venv
```

### 激活虚拟环境

#### Windows
```bash
venv\Scripts\activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

### 退出虚拟环境

```bash
deactivate
```

### 删除虚拟环境

直接删除venv目录即可：

```bash
# Windows
rmdir /s /q venv

# macOS/Linux
rm -rf venv
```

## 其他虚拟环境工具

除了venv，还有其他虚拟环境管理工具：

- **virtualenv**：功能更丰富的虚拟环境工具
  ```bash
  pip install virtualenv
  virtualenv venv
  ```

- **conda**：科学计算领域常用的环境管理工具
  ```bash
  conda create -n venv python=3.8
  conda activate venv
  ```

- **pipenv**：结合了pip和virtualenv的功能
  ```bash
  pip install pipenv
  pipenv install
  ```

- **poetry**：现代化的Python项目管理工具
  ```bash
  pip install poetry
  poetry init
  ```

## 项目结构最佳实践

1. **模块化设计**：将代码分成多个模块和包，提高代码的可维护性
2. **关注点分离**：不同功能的代码放在不同的文件中
3. **src布局**：源代码放在src目录下，便于打包和安装
4. **配置管理**：使用配置文件或环境变量管理配置
5. **版本控制**：使用Git进行版本控制
6. **文档**：为代码添加文档字符串和使用说明
7. **测试**：编写单元测试和集成测试

## 许可证

本项目使用MIT许可证。