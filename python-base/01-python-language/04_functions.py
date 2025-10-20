#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数示例

print("Python 函数示例\n" + "="*50)

# 1. 基本函数定义与调用
print("\n1. 基本函数定义与调用")

def greet():
    """这是一个简单的问候函数（文档字符串）"""
    print("Hello, Python!")

# 调用函数
greet()
# 查看函数文档
print(f"函数文档: {greet.__doc__}")

# 2. 带参数的函数
print("\n2. 带参数的函数")

def greet_name(name):
    """带参数的问候函数"""
    print(f"Hello, {name}!")

# 位置参数调用
greet_name("Alice")

# 3. 函数返回值
print("\n3. 函数返回值")

def add(a, b):
    """返回两个数的和"""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# 4. 函数中的参数类型
print("\n4. 函数中的参数类型")

# 4.1 默认参数
def greet_person(name, greeting="Hello"):
    """带默认参数的问候函数"""
    print(f"{greeting}, {name}!")

print("默认参数:")
greet_person("Bob")  # 使用默认问候语
greet_person("Bob", "Hi")  # 自定义问候语

# 4.2 关键字参数
def describe_person(name, age, city):
    """使用关键字参数的函数"""
    print(f"姓名: {name}, 年龄: {age}, 城市: {city}")

print("\n关键字参数:")
describe_person(name="Charlie", age=30, city="New York")
describe_person(age=25, city="London", name="David")  # 可以改变参数顺序

# 4.3 位置可变参数 (*args)
def sum_numbers(*args):
    """接收任意数量的位置参数"""
    print(f"参数列表: {args}")
    return sum(args)

print("\n位置可变参数 (*args):")
print(f"sum_numbers(1, 2, 3): {sum_numbers(1, 2, 3)}")
print(f"sum_numbers(1, 2, 3, 4, 5): {sum_numbers(1, 2, 3, 4, 5)}")

# 4.4 关键字可变参数 (**kwargs)
def print_info(**kwargs):
    """接收任意数量的关键字参数"""
    print(f"关键字参数字典: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n关键字可变参数 (**kwargs):")
print_info(name="Eve", age=28, city="Paris", job="Developer")

# 4.5 混合使用不同类型的参数
def mixed_params(a, b, *args, c=10, **kwargs):
    """混合使用不同类型的参数"""
    print(f"位置参数 a: {a}, b: {b}")
    print(f"可变位置参数 args: {args}")
    print(f"默认参数 c: {c}")
    print(f"可变关键字参数 kwargs: {kwargs}")

print("\n混合使用不同类型的参数:")
mixed_params(1, 2, 3, 4, c=20, d=5, e=6)

# 5. 匿名函数 (lambda)
print("\n5. 匿名函数 (lambda)")

# 基本lambda函数
square = lambda x: x ** 2
print(f"lambda 函数计算平方: square(5) = {square(5)}")

# lambda函数用作参数
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"使用 map() 和 lambda 计算平方: {squared_numbers}")

# 使用lambda函数进行排序
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students_sorted = sorted(students, key=lambda student: student[1])  # 按分数排序
print(f"按分数排序的学生列表: {students_sorted}")

# 6. 闭包
print("\n6. 闭包")

def outer_function(x):
    """外部函数，返回内部函数"""
    def inner_function(y):
        """内部函数，可以访问外部函数的变量"""
        return x + y
    return inner_function  # 返回内部函数，不调用

# 创建闭包
add_five = outer_function(5)
add_ten = outer_function(10)

print(f"闭包 add_five(3): {add_five(3)}")  # 5 + 3 = 8
print(f"闭包 add_ten(3): {add_ten(3)}")  # 10 + 3 = 13

# 7. 局部变量和全局变量
print("\n7. 局部变量和全局变量")

# 全局变量
global_var = "我是全局变量"

def demonstrate_scope():
    # 修改全局变量需要使用 global 关键字
    global global_var

    # 局部变量
    local_var = "我是局部变量"
    print(f"函数内部访问局部变量: {local_var}")
    print(f"函数内部访问全局变量: {global_var}")

    global_var = "全局变量被修改了"

    # 定义与全局变量同名的局部变量
    # 注意：这不会修改全局变量，而是创建一个新的局部变量
    shadow_var = "全局影子变量的值"
    print(f"函数内部的影子变量: {shadow_var}")

demonstrate_scope()
print(f"函数外部访问全局变量: {global_var}")

# 8. nonlocal 关键字
print("\n8. nonlocal 关键字")

def outer():
    x = "outer x"

    def inner():
        nonlocal x  # 使用 nonlocal 访问外部函数的变量
        x = "inner x"
        print(f"inner 函数中的 x: {x}")

    print(f"调用 inner 前，outer 函数中的 x: {x}")
    inner()
    print(f"调用 inner 后，outer 函数中的 x: {x}")

outer()

# 9. 函数作为参数传递
print("\n9. 函数作为参数传递")

def apply_function(func, value):
    """接收一个函数和一个值，将函数应用于该值"""
    return func(value)

result = apply_function(square, 6)
print(f"将 square 函数作为参数传递: apply_function(square, 6) = {result}")

# 使用 lambda 函数作为参数
result = apply_function(lambda x: x * 2, 6)
print(f"将 lambda 函数作为参数传递: apply_function(lambda x: x*2, 6) = {result}")

# 10. 函数作为返回值
print("\n10. 函数作为返回值")

def create_operation(operation):
    """根据操作类型返回不同的函数"""
    if operation == "add":
        return lambda a, b: a + b
    elif operation == "subtract":
        return lambda a, b: a - b
    elif operation == "multiply":
        return lambda a, b: a * b
    elif operation == "divide":
        return lambda a, b: a / b if b != 0 else "除数不能为零"

add_func = create_operation("add")
subtract_func = create_operation("subtract")

print(f"add_func(5, 3) = {add_func(5, 3)}")
print(f"subtract_func(5, 3) = {subtract_func(5, 3)}")

# 11. 递归函数
print("\n11. 递归函数")

def factorial(n):
    """计算阶乘的递归函数"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")

# 12. 函数注解
print("\n12. 函数注解")

def greet_with_annotations(name: str, age: int = 0) -> str:
    """带注解的函数"""
    return f"Hello, {name}! You are {age} years old."

print(greet_with_annotations("Frank", 30))
print(f"函数注解: {greet_with_annotations.__annotations__}")