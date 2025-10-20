#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"这是 sample_package 的 __init__.py 文件"

# 包级别变量
greeting = "Hello from sample_package!"

# 可以在 __init__.py 中导入子模块或子包
def package_function():
    "包级别的函数"
    return "This is a function defined in the package's __init__.py"

# 定义 __all__ 列表，控制 'from sample_package import *' 的行为
__all__ = ['module1', 'module2', 'greeting', 'package_function']