#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"这是 sample_package 的 module1 模块"

def function1():
    "module1 中的函数"
    return "This is function1 from module1"

class Class1:
    "module1 中的类"
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

# 模块级别的变量
module1_var = "I am a variable in module1"