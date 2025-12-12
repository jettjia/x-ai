#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 运算符示例

print("Python 运算符示例\n" + "="*50)

# 1. 算术运算符
a = 10
b = 3

print("\n1. 算术运算符")
print(f"{a} + {b} = {a + b}")  # 加法
print(f"{a} - {b} = {a - b}")  # 减法
print(f"{a} * {b} = {a * b}")  # 乘法
print(f"{a} / {b} = {a / b}")  # 除法（总是返回浮点数）
print(f"{a} // {b} = {a // b}")  # 整除（地板除）
print(f"{a} % {b} = {a % b}")  # 取模（余数）
print(f"{a} ** {b} = {a ** b}")  # 幂运算

# 2. 比较运算符
x = 5
y = 10

print("\n2. 比较运算符")
print(f"{x} == {y}: {x == y}")  # 等于
print(f"{x} != {y}: {x != y}")  # 不等于
print(f"{x} > {y}: {x > y}")  # 大于
print(f"{x} < {y}: {x < y}")  # 小于
print(f"{x} >= {y}: {x >= y}")  # 大于等于
print(f"{x} <= {y}: {x <= y}")  # 小于等于

# 3. 赋值运算符
z = 10
print("\n3. 赋值运算符")
print(f"初始 z = {z}")
z += 5
print(f"z += 5: {z}")  # 加法赋值
z -= 3
print(f"z -= 3: {z}")  # 减法赋值
z *= 2
print(f"z *= 2: {z}")  # 乘法赋值
z /= 4
print(f"z /= 4: {z}")  # 除法赋值
z //= 2
print(f"z //= 2: {z}")  # 整除赋值
z %= 3
print(f"z %= 3: {z}")  # 取模赋值
z **= 2
print(f"z **= 2: {z}")  # 幂运算赋值

# 4. 位运算符
p = 10  # 二进制: 1010
q = 4   # 二进制: 0100

print("\n4. 位运算符")
print(f"p = {p} (二进制: {bin(p)})\nq = {q} (二进制: {bin(q)})")
print(f"p & q = {p & q} (二进制: {bin(p & q)})  # 按位与")
print(f"p | q = {p | q} (二进制: {bin(p | q)})  # 按位或")
print(f"p ^ q = {p ^ q} (二进制: {bin(p ^ q)})  # 按位异或")
print(f"~p = {~p} (二进制: {bin(~p)})  # 按位非")
print(f"p << 1 = {p << 1} (二进制: {bin(p << 1)})  # 左移")
print(f"p >> 1 = {p >> 1} (二进制: {bin(p >> 1)})  # 右移")

# 5. 逻辑运算符
logical_a = True
logical_b = False

print("\n5. 逻辑运算符")
print(f"{logical_a} and {logical_b}: {logical_a and logical_b}")  # 逻辑与
print(f"{logical_a} or {logical_b}: {logical_a or logical_b}")    # 逻辑或
print(f"not {logical_a}: {not logical_a}")                      # 逻辑非

# 短路逻辑示例
print("\n短路逻辑示例:")
print("False and print('不会执行'): ", end="")
False and print("不会执行")  # 由于第一个操作数为False，and短路，第二个操作数不会执行

print("True or print('不会执行'): ", end="")
True or print("不会执行")    # 由于第一个操作数为True，or短路，第二个操作数不会执行

# 6. 成员运算符
my_list = [1, 2, 3, 4, 5]
my_str = "Hello, Python!"

print("\n6. 成员运算符")
print(f"3 in {my_list}: {3 in my_list}")
print(f"6 in {my_list}: {6 in my_list}")
print(f"'H' in '{my_str}': {'H' in my_str}")
print(f"'world' in '{my_str}': {'world' in my_str}")
print(f"3 not in {my_list}: {3 not in my_list}")
print(f"6 not in {my_list}: {6 not in my_list}")

# 7. 身份运算符
obj1 = [1, 2, 3]
obj2 = [1, 2, 3]
obj3 = obj1

print("\n7. 身份运算符")
print(f"obj1 = {obj1}\nobj2 = {obj2}\nobj3 = obj1")
print(f"obj1 is obj2: {obj1 is obj2}")  # obj1和obj2内容相同但不是同一对象
print(f"obj1 is obj3: {obj1 is obj3}")  # obj1和obj3是同一对象
print(f"obj1 == obj2: {obj1 == obj2}")  # 内容比较
print(f"obj1 is not obj2: {obj1 is not obj2}")

# 8. 运算符优先级示例
print("\n8. 运算符优先级示例")
print(f"3 + 4 * 2 = {3 + 4 * 2}")  # 乘法优先级高于加法
print(f"(3 + 4) * 2 = {(3 + 4) * 2}")  # 使用括号改变优先级
print(f"2 ** 3 * 4 = {2 ** 3 * 4}")  # 幂运算优先级高于乘法
print(f"2 * 3 ** 4 = {2 * 3 ** 4}")  # 幂运算优先级高于乘法
print(f"10 % 4 + 2 = {10 % 4 + 2}")  # 取模和加法优先级
print(f"10 % (4 + 2) = {10 % (4 + 2)}")  # 使用括号改变优先级

# 9. 字符串运算符
str1 = "Hello"
str2 = "Python"

print("\n9. 字符串运算符")
print(f"{str1} + {str2} = {str1 + str2}")  # 字符串连接
print(f"{str1} * 3 = {str1 * 3}")         # 字符串重复

# 10. 列表运算符
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("\n10. 列表运算符")
print(f"{list1} + {list2} = {list1 + list2}")  # 列表连接
print(f"{list1} * 2 = {list1 * 2}")           # 列表重复

# 11. 三元运算符
print("\n11. 三元运算符")
result = "大于5" if x > 5 else "小于等于5"
print(f"{x} {result}")

# 12. 链式比较
print("\n12. 链式比较")
print(f"1 < {x} < 10: {1 < x < 10}")
print(f"0 <= {x} <= 5: {0 <= x <= 5}")