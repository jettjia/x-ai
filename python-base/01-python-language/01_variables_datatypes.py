#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 变量与类型示例

# 1. 声明各种数据类型的变量

# 整数类型
integer_var = 42
print(f"整数类型: {integer_var}, 类型: {type(integer_var)}")

# 浮点数类型
float_var = 3.14159
print(f"浮点数类型: {float_var}, 类型: {type(float_var)}")

# 复数类型
complex_var = 1 + 2j
print(f"复数类型: {complex_var}, 类型: {type(complex_var)}")

# 布尔类型
bool_var = True
print(f"布尔类型: {bool_var}, 类型: {type(bool_var)}")

# 字符串类型
string_var = "Hello, Python!"
print(f"字符串类型: {string_var}, 类型: {type(string_var)}")

# 字节类型
bytes_var = b"Hello"
print(f"字节类型: {bytes_var}, 类型: {type(bytes_var)}")

# 列表类型
list_var = [1, 2, 3, "Python", True]
print(f"列表类型: {list_var}, 类型: {type(list_var)}")

# 元组类型
tuple_var = (1, 2, 3, "Python", False)
print(f"元组类型: {tuple_var}, 类型: {type(tuple_var)}")

# 集合类型
set_var = {1, 2, 3, 3, 4}
print(f"集合类型: {set_var}, 类型: {type(set_var)}")

# 字典类型
dict_var = {"name": "Python", "version": 3.10, "is_fun": True}
print(f"字典类型: {dict_var}, 类型: {type(dict_var)}")

# 空类型
none_var = None
print(f"空类型: {none_var}, 类型: {type(none_var)}")

print("\n" + "="*50 + "\n")

# 2. 类型转换案例

# 整数转换
a = "123"
b = int(a)
print(f"字符串转整数: '{a}' -> {b}, 类型: {type(b)}")

# 浮点数转换
c = 42
d = float(c)
print(f"整数转浮点数: {c} -> {d}, 类型: {type(d)}")

# 字符串转换
e = 3.14
f = str(e)
print(f"浮点数转字符串: {e} -> '{f}', 类型: {type(f)}")

# 布尔转换
g = 0
h = bool(g)
print(f"0转布尔值: {g} -> {h}, 类型: {type(h)}")

i = 100
j = bool(i)
print(f"非0数转布尔值: {i} -> {j}, 类型: {type(j)}")

# 列表转换
k = "Python"
l = list(k)
print(f"字符串转列表: '{k}' -> {l}, 类型: {type(l)}")

# 元组转换
m = [1, 2, 3]
n = tuple(m)
print(f"列表转元组: {m} -> {n}, 类型: {type(n)}")

# 集合转换
o = (1, 2, 2, 3)
p = set(o)
print(f"元组转集合: {o} -> {p}, 类型: {type(p)}")

# 字典转换 - 使用键值对列表
q = [("name", "Alice"), ("age", 30)]
r = dict(q)
print(f"键值对列表转字典: {q} -> {r}, 类型: {type(r)}")

# 复数转换
s = 5
t = complex(s)
u = complex(s, 7)
print(f"整数转复数: {s} -> {t}")
print(f"两个整数转复数: {s}, {7} -> {u}")

print("\n" + "="*50 + "\n")

# 3. 类型检查和 isinstance() 函数

# 使用 isinstance() 检查类型
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"isinstance(3.14, float): {isinstance(3.14, float)}")
print(f"isinstance('Python', str): {isinstance('Python', str)}")
print(f"isinstance([], list): {isinstance([], list)}")
print(f"isinstance((), tuple): {isinstance((), tuple)}")
print(f"isinstance({{}}, dict): {isinstance({}, dict)}")

# 检查是否是数值类型
print(f"isinstance(42, (int, float, complex)): {isinstance(42, (int, float, complex))}")
print(f"isinstance('Python', (int, float, complex)): {isinstance('Python', (int, float, complex))}")

print("\n" + "="*50 + "\n")

# 4. Python 中的动态类型特性

# 同一个变量可以改变类型
x = 100
print(f"x 初始值: {x}, 类型: {type(x)}")

x = "现在我是字符串"
print(f"x 改变后: {x}, 类型: {type(x)}")

x = [1, 2, 3]
print(f"x 再次改变: {x}, 类型: {type(x)}")