#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 异常处理示例

print("Python 异常处理示例\n" + "="*50)

# 1. 基本的 try-except 结构
print("\n1. 基本的 try-except 结构")

try:
    # 尝试执行可能引发异常的代码
    result = 10 / 0
    print("这行代码不会执行")
except ZeroDivisionError:
    # 处理特定类型的异常
    print("捕获到 ZeroDivisionError: 除数不能为零")

print("程序继续执行...")

# 2. 捕获多种类型的异常
print("\n2. 捕获多种类型的异常")

try:
    # 尝试将用户输入转换为整数并进行除法运算
    num1 = int(input("请输入第一个数字: "))  # 可能引发 ValueError
    num2 = int(input("请输入第二个数字: "))  # 可能引发 ValueError
    result = num1 / num2  # 可能引发 ZeroDivisionError
    print(f"结果: {result}")
except ZeroDivisionError:
    print("错误: 除数不能为零")
except ValueError:
    print("错误: 请输入有效的数字")

# 3. 捕获所有异常
print("\n3. 捕获所有异常")

try:
    # 可能引发任何异常的代码
    my_list = [1, 2, 3]
    print(my_list[10])  # 索引越界，引发 IndexError
except:
    # 捕获所有异常
    print("捕获到异常，但不知道具体类型")

# 4. 获取异常信息
print("\n4. 获取异常信息")

try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])  # 键不存在，引发 KeyError
except KeyError as e:
    print(f"捕获到 KeyError: {e}")
    print(f"异常类型: {type(e).__name__}")

# 5. 多个 except 块
print("\n5. 多个 except 块")

try:
    # 尝试打开一个不存在的文件
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("错误: 文件未找到")
except PermissionError:
    print("错误: 没有权限访问文件")
except Exception as e:
    # 捕获其他所有异常
    print(f"发生未知错误: {e}")

# 6. else 子句
print("\n6. else 子句")

try:
    # 如果没有异常发生，else 子句将被执行
    result = 10 / 2
except ZeroDivisionError:
    print("除数不能为零")
else:
    # 只有在没有异常时才会执行
    print(f"计算成功，结果: {result}")

# 7. finally 子句
print("\n7. finally 子句")

try:
    # finally 子句无论是否发生异常都会执行
    file = open("sample.txt", "w")
    file.write("Hello, World!")
    # 故意引发异常
    1/0
except ZeroDivisionError:
    print("捕获到 ZeroDivisionError")
finally:
    # 确保文件被关闭
    print("执行 finally 子句，关闭文件")
    file.close()

# 8. 使用 with 语句自动管理资源（上下文管理器）
print("\n8. 使用 with 语句自动管理资源")

try:
    # with 语句会自动调用文件的 __enter__ 和 __exit__ 方法
    with open("sample.txt", "r") as file:
        content = file.read()
        print(f"文件内容: {content}")
        # 故意引发异常
        1/0
except ZeroDivisionError:
    print("捕获到 ZeroDivisionError")
    # 即使发生异常，with 语句也会确保文件被关闭

# 9. 自定义异常
print("\n9. 自定义异常")

# 自定义异常类，继承自 Exception
class InsufficientFundsError(Exception):
    """当余额不足时引发的异常"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"余额不足: 当前余额 {balance}，尝试取出 {amount}"
        super().__init__(self.message)

# 使用自定义异常
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    current_balance = 100
    withdrawal_amount = 150
    new_balance = withdraw(current_balance, withdrawal_amount)
    print(f"取款成功，新余额: {new_balance}")
except InsufficientFundsError as e:
    print(f"错误: {e}")
    print(f"余额: {e.balance}, 尝试取出: {e.amount}")

# 10. 异常链
print("\n10. 异常链")

try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        # 使用 raise ... from 保留原始异常信息
        raise ValueError("处理除法时出错") from e
except ValueError as e:
    print(f"捕获到 ValueError: {e}")
    # 打印异常链
    print("异常链:")
    while e:
        print(f"- {type(e).__name__}: {e}")
        e = e.__cause__  # 获取原始异常

# 11. 异常处理的嵌套
print("\n11. 异常处理的嵌套")

try:
    print("外层 try 开始")
    try:
        print("内层 try 开始")
        result = 10 / 0
        print("内层 try 结束")  # 不会执行
    except ZeroDivisionError:
        print("内层 except: 捕获到除数为零异常")
        # 可以选择重新引发异常
        # raise
    print("外层 try 继续执行")
except Exception as e:
    print(f"外层 except: 捕获到异常: {e}")
finally:
    print("外层 finally 执行")

# 12. 使用 assert 语句进行断言
print("\n12. 使用 assert 语句进行断言")

def calculate_discount(price, discount):
    # 断言确保折扣在合理范围内
    assert 0 <= discount <= 1, "折扣必须在0到1之间"
    return price * (1 - discount)

try:
    discounted_price = calculate_discount(100, 1.5)  # 折扣超出范围
    print(f"折扣后价格: {discounted_price}")
except AssertionError as e:
    print(f"断言失败: {e}")

# 注意：运行 Python 时使用 -O 选项可以禁用断言

# 13. 使用 warnings 模块发出警告
print("\n13. 使用 warnings 模块发出警告")

import warnings

# 发出警告
warnings.warn("这是一个警告消息")

# 可以过滤警告
def deprecated_function():
    warnings.warn("此函数已过时，请使用新函数", DeprecationWarning)
    return "旧函数的结果"

# 抑制特定类型的警告
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    result = deprecated_function()
    print(f"调用已过时函数的结果: {result}")

# 14. 常见的内置异常类型
print("\n14. 常见的内置异常类型")

common_exceptions = [
    ZeroDivisionError,  # 除数为零
    ValueError,         # 值错误
    TypeError,          # 类型错误
    IndexError,         # 索引错误
    KeyError,           # 键错误
    FileNotFoundError,  # 文件未找到
    PermissionError,    # 权限错误
    MemoryError,        # 内存错误
    OverflowError,      # 溢出错误
    ImportError,        # 导入错误
    RuntimeError        # 运行时错误
]

print("常见的内置异常类型:")
for exc in common_exceptions:
    print(f"- {exc.__name__}: {exc.__doc__}")

# 15. 异常处理的最佳实践
print("\n15. 异常处理的最佳实践")

print("异常处理的最佳实践:")
print("1. 只捕获你能处理的异常")
print("2. 使用具体的异常类型，而不是通用的 Exception")
print("3. 使用 with 语句自动管理资源")
print("4. 在 finally 子句中释放资源")
print("5. 提供有意义的错误信息")
print("6. 避免过度使用异常来控制程序流程")
print("7. 对于预期的错误情况，考虑使用条件检查而不是异常")
print("8. 为你的模块定义自定义异常类")