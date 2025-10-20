#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project Template Package

这是一个Python项目模板包，用于演示如何创建一个结构良好的Python项目。
"""

# 从子模块导入函数
from .main import hello_world, create_project_structure

# 定义包的版本
__version__ = '0.1.0'

# 定义公共API
__all__ = [
    'hello_world',
    'create_project_structure',
    '__version__'
]