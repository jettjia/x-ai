#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"这是 sample_package 的 module2 模块"

def function2():
    "module2 中的函数"
    return "This is function2 from module2"

# 从同一包中导入其他模块
from . import module1

# 使用来自 module1 的功能
def use_module1():
    result = module1.function1()
    instance = module1.Class1("Created from module2")
    return f"module2 使用 module1: {result}, {instance.get_name()}"