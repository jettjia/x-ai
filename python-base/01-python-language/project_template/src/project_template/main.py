#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""主模块文件

包含项目的主要功能函数。
"""
import os
import sys


def hello_world():
    """一个简单的示例函数
    
    Returns:
        str: 问候消息
    """
    return "Hello, World!"


def create_project_structure(project_name, base_dir=None):
    """创建一个标准的Python项目结构
    
    Args:
        project_name (str): 项目名称
        base_dir (str, optional): 基础目录路径。默认为当前目录。
        
    Returns:
        str: 创建的项目路径
        
    Raises:
        OSError: 当创建目录失败时
    """
    # 如果没有提供基础目录，使用当前目录
    if base_dir is None:
        base_dir = os.getcwd()
    
    # 构建完整的项目路径
    project_path = os.path.join(base_dir, project_name)
    
    # 定义项目结构
    directories = [
        os.path.join(project_path, 'src', project_name),
        os.path.join(project_path, 'tests'),
        os.path.join(project_path, 'data'),
        os.path.join(project_path, 'docs'),
    ]
    
    # 创建目录结构
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # 创建__init__.py文件在包目录中
        if directory.endswith(os.path.join('src', project_name)):
            with open(os.path.join(directory, '__init__.py'), 'w') as f:
                f.write('"""{} Package"""\n\n'.format(project_name.capitalize()))
                f.write('# 从子模块导入函数\n')
                f.write('# from .main import your_function\n\n')
                f.write('# 定义包的版本\n')
                f.write('__version__ = \'0.1.0\'\n\n')
                f.write('# 定义公共API\n')
                f.write('__all__ = [\n')
                f.write('    # \'your_function\',\n')
                f.write('    \'__version__\'\n')
                f.write(']\n')
        
        # 创建__init__.py文件在测试目录中
        elif directory.endswith('tests'):
            with open(os.path.join(directory, '__init__.py'), 'w') as f:
                f.write('"""测试模块"""\n')
    
    # 创建主模块文件
    main_file = os.path.join(project_path, 'src', project_name, 'main.py')
    with open(main_file, 'w') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n\n')
        f.write('"""主模块文件\n\n')
        f.write('包含项目的主要功能函数。\n')
        f.write('"""\n\n')
        f.write('def main():\n')
        f.write('    """主函数"""\n')
        f.write('    print("Hello from {}")\n'.format(project_name))
        f.write('\n')
        f.write('if __name__ == "__main__":\n')
        f.write('    main()\n')
    
    # 创建setup.py文件
    setup_file = os.path.join(project_path, 'setup.py')
    with open(setup_file, 'w') as f:
        f.write('from setuptools import setup, find_packages\n\n')
        f.write('setup(\n')
        f.write('    name=\'{}\',\n'.format(project_name))
        f.write('    version=\'0.1.0\',\n')
        f.write('    packages=find_packages(\'src\'),\n')
        f.write('    package_dir={\'\': \'src\'},\n')
        f.write('    install_requires=[\n')
        f.write('        # 项目依赖\n')
        f.write('    ],\n')
        f.write('    entry_points={\n')
        f.write('        \'console_scripts\': [\n')
        f.write('            \'{0}={0}.main:main\'\n'.format(project_name))
        f.write('        ],\n')
        f.write('    },\n')
        f.write(')\n')
    
    # 创建requirements.txt文件
    requirements_file = os.path.join(project_path, 'requirements.txt')
    with open(requirements_file, 'w') as f:
        f.write('# 项目依赖列表\n')
        f.write('# 使用命令 "pip freeze > requirements.txt" 生成\n')
    
    # 创建README.md文件
    readme_file = os.path.join(project_path, 'README.md')
    with open(readme_file, 'w') as f:
        f.write('# {}\n\n'.format(project_name.replace('_', ' ').title()))
        f.write('A simple Python project.\n\n')
        f.write('## Installation\n\n')
        f.write('```bash\n')
        f.write('# Clone the repository\n')
        f.write('git clone <repository-url>\n')
        f.write('cd {}\n\n'.format(project_name))
        f.write('# Create and activate virtual environment\n')
        f.write('python -m venv venv\n')
        f.write('source venv/bin/activate  # On Windows: venv\\Scripts\\activate\n\n')
        f.write('# Install dependencies\n')
        f.write('pip install -r requirements.txt\n')
        f.write('```\n\n')
        f.write('## Usage\n\n')
        f.write('```python\n')
        f.write('# Example usage\n')
        f.write('from {} import your_function\n'.format(project_name))
        f.write('\n')
        f.write('# Call your function\n')
        f.write('# result = your_function()\n')
        f.write('```\n')
    
    # 创建.gitignore文件
    gitignore_file = os.path.join(project_path, '.gitignore')
    with open(gitignore_file, 'w') as f:
        f.write('# Virtual environments\n')
        f.write('venv/\n')
        f.write('env/\n')
        f.write('*.venv\n\n')
        f.write('# IDE configurations\n')
        f.write('.idea/\n')
        f.write('.vscode/\n')
        f.write('*.swp\n')
        f.write('*.swo\n')
        f.write('*~\n')
        f.write('.DS_Store\n\n')
        f.write('# Python cache\n')
        f.write('__pycache__/\n')
        f.write('*.pyc\n')
        f.write('*.pyo\n')
        f.write('*.pyd\n\n')
        f.write('# Test and coverage\n')
        f.write('.coverage\n')
        f.write('coverage.xml\n')
        f.write('htmlcov/\n')
        f.write('pytest_cache/\n\n')
        f.write('# Build\n')
        f.write('build/\n')
        f.write('dist/\n')
        f.write('*.egg-info/\n\n')
        f.write('# Logs\n')
        f.write('*.log\n')
    
    # 返回创建的项目路径
    return project_path


if __name__ == '__main__':
    # 示例用法
    print(hello_world())