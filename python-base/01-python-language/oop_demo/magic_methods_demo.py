#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""魔法方法演示模块 - 展示Python的特殊方法"""

import math

class Vector:
    """Vector 类 - 演示各种魔法方法"""
    
    def __init__(self, x, y):
        """构造函数 - 初始化向量的坐标"""
        self.x = x
        self.y = y
    
    # 字符串表示方法
    def __str__(self):
        """返回向量的字符串表示 - 用于 str() 和 print()"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """返回向量的正式字符串表示 - 用于 repr()"""
        return f"Vector({self.x}, {self.y})"
    
    # 运算符重载
    def __add__(self, other):
        """重载加法运算符 +"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """重载减法运算符 -"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """重载乘法运算符 *"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    # 比较运算符
    def __eq__(self, other):
        """重载相等运算符 =="""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __lt__(self, other):
        """重载小于运算符 <"""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        return NotImplemented
    
    # 容器相关方法
    def __len__(self):
        """重载 len() 函数 - 返回向量的维数"""
        return 2  # 二维向量
    
    def __getitem__(self, index):
        """重载索引访问 - 允许使用 vector[0], vector[1]"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        """重载索引赋值 - 允许使用 vector[0] = x, vector[1] = y"""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")
    
    # 其他有用的魔法方法
    def __abs__(self):
        """重载 abs() 函数 - 返回向量的模长"""
        return self.magnitude()
    
    def __bool__(self):
        """重载布尔转换 - 零向量返回 False"""
        return self.x != 0 or self.y != 0
    
    def __call__(self, scalar):
        """使向量对象可以像函数一样被调用"""
        return Vector(self.x * scalar, self.y * scalar)
    
    # 辅助方法
    def magnitude(self):
        """计算向量的模长"""
        return math.sqrt(self.x**2 + self.y**2)

class Book:
    """Book 类 - 演示上下文管理器和迭代器魔法方法"""
    
    def __init__(self, title, author, pages):
        """构造函数 - 初始化书籍信息"""
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
    
    def __str__(self):
        """返回书籍的字符串表示"""
        return f"{self.title} by {self.author} ({self.pages} pages)"
    
    # 上下文管理器方法
    def __enter__(self):
        """进入上下文管理器时调用"""
        print(f"Opening book '{self.title}'...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器时调用"""
        if exc_type is not None:
            print(f"Error reading book: {exc_val}")
        else:
            print(f"Closing book '{self.title}'...")
        # 返回 False 表示不抑制异常
        return False
    
    # 迭代器方法
    def __iter__(self):
        """使对象成为可迭代对象"""
        self.current_page = 0
        return self
    
    def __next__(self):
        """迭代器的下一个元素"""
        self.current_page += 1
        if self.current_page > self.pages:
            raise StopIteration
        return f"Page {self.current_page}: Content for page {self.current_page} of '{self.title}'"