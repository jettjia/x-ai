#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"这是 sample_package.subpackage 的 submodule 模块"

def submodule_function():
    "submodule 中的函数"
    return "This is submodule_function from submodule"

# 从父包导入（相对导入）
from .. import module1
from ..module2 import use_module1

# 使用来自父包的功能
def use_parent_modules():
    result1 = module1.function1()
    result2 = use_module1()
    return f"submodule 使用父包: {result1}, {result2}"