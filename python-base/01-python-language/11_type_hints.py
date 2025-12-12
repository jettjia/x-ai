#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python类型提示示例

print("Python 类型提示示例\n" + "="*50)

# 1. 什么是类型提示
print("\n1. 什么是类型提示")
print("- Python是动态类型语言，但从Python 3.5开始支持类型提示(Type Hints)")
print("- 类型提示允许开发者为变量、函数参数和返回值标注预期的类型")
print("- 类型提示不会改变Python的动态类型特性，它们只是提示，不是强制约束")
print("- 类型提示可以提高代码可读性，帮助IDE提供更好的自动补全和错误提示")
print("- 类型提示可以通过静态类型检查工具（如mypy）进行验证")

# 2. 基本类型标注
print("\n2. 基本类型标注")

# 变量类型标注
a: int = 10
b: float = 3.14
c: str = "Hello, Python!"
d: bool = True
e: None = None

print(f"整数变量: a = {a}, 类型: {type(a).__name__}")
print(f"浮点数变量: b = {b}, 类型: {type(b).__name__}")
print(f"字符串变量: c = {c}, 类型: {type(c).__name__}")
print(f"布尔值变量: d = {d}, 类型: {type(d).__name__}")
print(f"None变量: e = {e}, 类型: {type(e).__name__}")

# 3. 函数参数和返回值类型标注
print("\n3. 函数参数和返回值类型标注")

def add_numbers(x: int, y: int) -> int:
    """计算两个整数的和并返回结果"""
    return x + y

def greet(name: str) -> str:
    """向指定名称的人问好"""
    return f"Hello, {name}!"

def is_even(num: int) -> bool:
    """检查一个数是否为偶数"""
    return num % 2 == 0

# 测试函数
sum_result: int = add_numbers(5, 3)
greeting: str = greet("World")
even_check: bool = is_even(4)

print(f"add_numbers(5, 3) = {sum_result}")
print(f'greet("World") = {greeting}')
print(f"is_even(4) = {even_check}")

# 4. 复杂类型标注
print("\n4. 复杂类型标注")

# 需要从typing模块导入复杂类型
from typing import List, Tuple, Dict, Set, Optional, Union, Any, Callable, Iterable

# 列表类型
numbers: List[int] = [1, 2, 3, 4, 5]
names: List[str] = ["Alice", "Bob", "Charlie"]
mixed_list: List[Union[int, str]] = [1, "two", 3, "four"]

# 元组类型
dimensions: Tuple[int, int, int] = (10, 20, 30)
point: Tuple[float, float] = (3.5, 7.2)

def get_user_info() -> Tuple[int, str, bool]:
    """返回用户信息"""
    return 1, "Alice", True

# 字典类型
user: Dict[str, Union[int, str, bool]] = {"id": 1, "name": "Alice", "active": True}
scores: Dict[str, float] = {"Alice": 95.5, "Bob": 88.0, "Charlie": 92.5}

# 集合类型
unique_numbers: Set[int] = {1, 2, 3, 4, 5}
unique_names: Set[str] = {"Alice", "Bob", "Charlie"}

# Optional类型 - 表示值可以是指定类型或None
optional_name: Optional[str] = "Alice"
optional_age: Optional[int] = None

# Union类型 - 表示值可以是多个指定类型中的任意一个
age_or_name: Union[int, str] = 25  # 也可以是字符串
result: Union[int, float, None] = 42  # 可以是整数、浮点数或None

# Any类型 - 表示可以是任何类型
data: Any = "This can be any type"
data = 100  # 现在是整数
data = [1, 2, 3]  # 现在是列表

# 打印复杂类型示例
print(f"整数列表: {numbers}")
print(f"混合类型列表: {mixed_list}")
print(f"元组: {dimensions}")
print(f"字典: {user}")
print(f"集合: {unique_numbers}")
print(f"Optional类型 (有值): {optional_name}")
print(f"Optional类型 (None值): {optional_age}")

# 5. 类型标注的高级用法
print("\n5. 类型标注的高级用法")

# 函数类型标注
operation: Callable[[int, int], int] = add_numbers
print(f"使用函数类型变量: operation(10, 20) = {operation(10, 20)}")

def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    """应用指定的操作到两个数"""
    return op(x, y)

result: int = apply_operation(8, 4, add_numbers)
print(f"apply_operation(8, 4, add_numbers) = {result}")

# 可迭代类型
def process_items(items: Iterable[int]) -> List[int]:
    """处理可迭代对象中的所有整数"""
    return [item * 2 for item in items]

processed_list: List[int] = process_items([1, 2, 3, 4, 5])
processed_tuple: List[int] = process_items((6, 7, 8, 9, 10))
processed_set: List[int] = process_items({11, 12, 13})

print(f"处理列表后的结果: {processed_list}")
print(f"处理元组后的结果: {processed_tuple}")
print(f"处理集合后的结果: {processed_set}")

# 6. 自定义类型和类型别名
print("\n6. 自定义类型和类型别名")

# 类型别名
type UserId = int
type Username = str
type Score = float

def update_user_score(user_id: UserId, score: Score) -> None:
    """更新用户分数"""
    print(f"用户ID {user_id} 的分数已更新为 {score}")

# 使用类型别名
user_id: UserId = 123
score: Score = 95.5
update_user_score(user_id, score)

# 复合类型别名
type User = Dict[Union[UserId, Username], Union[Score, bool, str]]

user1: User = {123: 95.5, "active": True, "name": "Alice"}
user2: User = {"Bob": 88.0, "active": False}

print(f"用户1信息: {user1}")
print(f"用户2信息: {user2}")

# 7. 泛型类型标注
print("\n7. 泛型类型标注")

from typing import TypeVar, Generic, List as TypingList

# 定义类型变量
T = TypeVar('T')  # 任意类型
KT = TypeVar('KT')  # 键类型
VT = TypeVar('VT')  # 值类型

# 泛型函数
def first_element(items: TypingList[T]) -> Optional[T]:
    """返回列表的第一个元素，如果列表为空则返回None"""
    return items[0] if items else None

# 使用泛型函数
first_str: Optional[str] = first_element(["apple", "banana", "cherry"])
first_int: Optional[int] = first_element([1, 2, 3, 4, 5])
first_empty: Optional[Any] = first_element([])

print(f"字符串列表的第一个元素: {first_str}")
print(f"整数列表的第一个元素: {first_int}")
print(f"空列表的第一个元素: {first_empty}")

# 泛型类
class Box(Generic[T]):
    """可以存储任意类型值的盒子"""
    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        """获取盒子中的值"""
        return self.value

    def set_value(self, value: T) -> None:
        """设置盒子中的值"""
        self.value = value

# 使用泛型类
int_box: Box[int] = Box(42)
str_box: Box[str] = Box("Hello")
list_box: Box[TypingList[int]] = Box([1, 2, 3])

print(f"整数盒子的值: {int_box.get_value()}")
print(f"字符串盒子的值: {str_box.get_value()}")
print(f"列表盒子的值: {list_box.get_value()}")

# 8. 类型标注与实际类型不匹配的情况
print("\n8. 类型标注与实际类型不匹配的情况")
print("注意：Python不会强制执行类型标注，以下代码虽然标注类型不匹配，但仍可运行")

# 类型标注与实际类型不匹配
wrong_type: int = "This is a string, not an int"
print(f"类型标注为int但实际为str的变量: {wrong_type}, 实际类型: {type(wrong_type).__name__}")

def wrong_return_type(x: int, y: int) -> int:
    return "This should return int but returns str"

result = wrong_return_type(1, 2)
print(f"标注返回int但实际返回str的函数结果: {result}, 实际类型: {type(result).__name__}")

# 9. 使用mypy进行静态类型检查
print("\n9. 使用mypy进行静态类型检查")
print("- mypy是一个静态类型检查工具，可以检查代码中的类型标注是否正确")
print("- 安装方法: pip install mypy")
print("- 使用方法: mypy filename.py")
print("- mypy会检查变量赋值、函数调用、返回值等是否符合类型标注")
print("- 对于上面类型标注不匹配的代码，mypy会给出警告")
print("- 可以使用mypy检查代码中的类型标注错误")
print("- 示例mypy输出:")
print("type_hints.py:180: error: Incompatible types in assignment (expression has type \"str\", variable has type \"int\")  [assignment]")
print("type_hints.py:185: error: Incompatible return value type (got \"str\", expected \"int\")  [return-value]")
print("Found 2 errors in 1 file (checked 1 source file)")

print("type_hints.py:180: error: Incompatible types in assignment (expression has type \"str\", variable has type \"int\")  [assignment]")
print("type_hints.py:185: error: Incompatible return value type (got \"str\", expected \"int\")  [return-value]")
print("Found 2 errors in 1 file (checked 1 source file)")

# 10. Python 3.10+ 的新类型标注语法
print("\n10. Python 3.10+ 的新类型标注语法")
print("- Python 3.10引入了更简洁的类型标注语法")
print("- 可以直接使用内置类型作为泛型，而不需要从typing模块导入")
print("\nPython 3.9+ 的新语法:")
print("\n# 列表类型")
print("numbers: list[int] = [1, 2, 3, 4, 5]")
print("\n# 元组类型")
print("dimensions: tuple[int, int, int] = (10, 20, 30)")
print("\n# 字典类型")
print("user: dict[str, Union[int, str, bool]] = {\"id\": 1, \"name\": \"Alice\", \"active\": True}")
print("\n# 集合类型")
print("unique_numbers: set[int] = {1, 2, 3, 4, 5}")
print("\n# 可选类型")
print("optional_name: str | None = \"Alice\"  # Python 3.10+")

# 11. 类型标注的最佳实践
print("\n11. 类型标注的最佳实践")
print("- 为公共API和复杂函数添加类型标注")
print("- 使用有意义的类型别名提高可读性")
print("- 对于简单的内部函数，类型标注可以简化或省略")
print("- 结合文档字符串使用，提供更完整的函数说明")
print("- 使用静态类型检查工具（如mypy）验证类型标注")
print("- 在团队项目中统一类型标注风格")
print("- 考虑项目的Python版本，选择合适的类型标注语法")

# 12. 更多类型标注示例
print("\n12. 更多类型标注示例")

# 嵌套数据结构
database: Dict[str, List[Dict[str, Union[int, str, List[str]]]]] = {
    "users": [
        {"id": 1, "name": "Alice", "roles": ["admin", "user"]},
        {"id": 2, "name": "Bob", "roles": ["user"]}
    ],
    "products": [
        {"id": 101, "name": "Laptop", "tags": ["electronics", "computer"]},
        {"id": 102, "name": "Phone", "tags": ["electronics", "mobile"]}
    ]
}

# 回调函数类型
def process_data(data: List[int], callback: Callable[[int], int]) -> List[int]:
    """对数据中的每个元素应用回调函数"""
    return [callback(item) for item in data]

def double(x: int) -> int:
    """返回输入值的两倍"""
    return x * 2

def square(x: int) -> int:
    """返回输入值的平方"""
    return x * x

doubled_data: List[int] = process_data([1, 2, 3, 4, 5], double)
squared_data: List[int] = process_data([1, 2, 3, 4, 5], square)

print(f"原始数据: [1, 2, 3, 4, 5]")
print(f"应用double函数后: {doubled_data}")
print(f"应用square函数后: {squared_data}")

# 生成器函数类型标注
def generate_numbers(n: int) -> Iterable[int]:
    """生成从1到n的整数"""
    for i in range(1, n+1):
        yield i

def generate_numbers_v2(n: int) -> "Generator[int, None, None]":
    """使用Generator类型标注生成器函数"""
    for i in range(1, n+1):
        yield i

# 注意：对于Python 3.9+，可以直接使用内置类型作为泛型
print("\n13. Python 3.9+ 的类型标注完整示例")
print("\n# 使用内置类型作为泛型")
print("def example_function(")
print("    numbers: list[int],")
print("    user: dict[str, str | int | bool],")
print("    options: set[str] = None,")
print(") -> tuple[list[int], dict[str, str | int | bool]]:")
print("    if options is None:")
print("        options = set()")
print("    return sorted(numbers), {k: v for k, v in user.items() if k not in options}")

print("\n总结：")
print("- 类型提示是Python的一个强大功能，可以提高代码可读性和可维护性")
print("- 类型提示不是强制约束，Python仍然是动态类型语言")
print("- 使用静态类型检查工具可以在运行前发现潜在问题")
print("- 随着Python版本的更新，类型提示语法也在不断改进和简化")