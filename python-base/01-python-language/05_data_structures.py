#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据结构示例

print("Python 数据结构示例\n" + "="*50)

# 1. 列表 (List)
print("\n1. 列表 (List)")

# 创建列表
my_list = [1, 2, 3, 4, 5]
print(f"初始列表: {my_list}")

# 查 - 访问元素
print(f"索引 0: {my_list[0]}")
print(f"索引 -1 (最后一个元素): {my_list[-1]}")
print(f"切片 [1:4]: {my_list[1:4]}")
print(f"切片 [2:]: {my_list[2:]}")
print(f"切片 [:3]: {my_list[:3]}")
print(f"切片 [::2] (步长为2): {my_list[::2]}")

# 增 - 添加元素
my_list.append(6)  # 在末尾添加元素
print(f"append(6) 后: {my_list}")

my_list.insert(2, 2.5)  # 在指定位置插入元素
print(f"insert(2, 2.5) 后: {my_list}")

my_list.extend([7, 8, 9])  # 扩展列表
print(f"extend([7, 8, 9]) 后: {my_list}")

# 改 - 修改元素
my_list[0] = 10
print(f"修改索引 0 为 10 后: {my_list}")

my_list[1:4] = [20, 30, 40]
print(f"修改切片 [1:4] 为 [20, 30, 40] 后: {my_list}")

# 删 - 删除元素
my_list.remove(40)  # 删除指定值的元素
print(f"remove(40) 后: {my_list}")

popped_element = my_list.pop()  # 弹出并返回最后一个元素
print(f"pop() 弹出元素: {popped_element}")
print(f"pop() 后: {my_list}")

popped_element = my_list.pop(1)  # 弹出并返回指定索引的元素
print(f"pop(1) 弹出元素: {popped_element}")
print(f"pop(1) 后: {my_list}")

del my_list[2]  # 删除指定索引的元素
print(f"del my_list[2] 后: {my_list}")

my_list.clear()  # 清空列表
print(f"clear() 后: {my_list}")

# 2. 元组 (Tuple)
print("\n2. 元组 (Tuple)")

# 创建元组
my_tuple = (1, 2, 3, 4, 5)
print(f"初始元组: {my_tuple}")

# 注意：单元素元组需要在元素后加逗号
single_tuple = (42,)
print(f"单元素元组: {single_tuple}, 类型: {type(single_tuple)}")

# 查 - 访问元素（与列表相同）
print(f"索引 0: {my_tuple[0]}")
print(f"切片 [1:4]: {my_tuple[1:4]}")

# 元组不可修改，尝试修改会引发错误
# my_tuple[0] = 10  # 这会引发 TypeError

# 可以通过转换为列表再修改，然后转回元组
temp_list = list(my_tuple)
temp_list[0] = 10
new_tuple = tuple(temp_list)
print(f"通过转换修改后的元组: {new_tuple}")

# 3. 集合 (Set)
print("\n3. 集合 (Set)")

# 创建集合
my_set = {1, 2, 3, 4, 5}
print(f"初始集合: {my_set}")

# 注意：创建空集合必须使用 set()
empty_set = set()
print(f"空集合: {empty_set}, 类型: {type(empty_set)}")

# 集合会自动去重
my_set = {1, 2, 2, 3, 4, 4, 5}
print(f"自动去重后的集合: {my_set}")

# 增 - 添加元素
my_set.add(6)
print(f"add(6) 后: {my_set}")

my_set.update([7, 8, 9])
print(f"update([7, 8, 9]) 后: {my_set}")

# 删 - 删除元素
my_set.remove(3)  # 如果元素不存在会引发 KeyError
print(f"remove(3) 后: {my_set}")

my_set.discard(10)  # 如果元素不存在不会引发错误
print(f"discard(10) 后: {my_set}")

popped_element = my_set.pop()  # 随机弹出一个元素
print(f"pop() 弹出元素: {popped_element}")
print(f"pop() 后: {my_set}")

my_set.clear()  # 清空集合
print(f"clear() 后: {my_set}")

# 集合运算
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"并集 (set1 | set2): {set1 | set2}")
print(f"交集 (set1 & set2): {set1 & set2}")
print(f"差集 (set1 - set2): {set1 - set2}")
print(f"对称差集 (set1 ^ set2): {set1 ^ set2}")

# 4. 字典 (Dictionary)
print("\n4. 字典 (Dictionary)")

# 创建字典
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"初始字典: {my_dict}")

# 使用 dict() 函数创建
my_dict2 = dict(name="Bob", age=25, city="London")
print(f"使用 dict() 创建的字典: {my_dict2}")

# 查 - 访问值
print(f"name 的值: {my_dict['name']}")
print(f"使用 get() 访问 name: {my_dict.get('name')}")
print(f"使用 get() 访问不存在的键: {my_dict.get('country', 'Unknown')}")

# 获取所有键、值、键值对
print(f"所有键: {list(my_dict.keys())}")
print(f"所有值: {list(my_dict.values())}")
print(f"所有键值对: {list(my_dict.items())}")

# 增 - 添加键值对
my_dict["country"] = "USA"
print(f"添加 country 后: {my_dict}")

# 改 - 修改值
my_dict["age"] = 31
print(f"修改 age 后: {my_dict}")

# 更新多个键值对
my_dict.update({"city": "Boston", "job": "Developer"})
print(f"update() 后: {my_dict}")

# 删 - 删除键值对
value = my_dict.pop("job")
print(f"pop('job') 弹出值: {value}")
print(f"pop('job') 后: {my_dict}")

# 随机删除并返回一个键值对
item = my_dict.popitem()
print(f"popitem() 弹出键值对: {item}")
print(f"popitem() 后: {my_dict}")

del my_dict["city"]
print(f"del my_dict['city'] 后: {my_dict}")

my_dict.clear()
print(f"clear() 后: {my_dict}")

# 5. 字符串 (String) - 虽然是基本类型，但也有很多操作
print("\n5. 字符串 (String)")

# 创建字符串
my_str = "Hello, Python!"
print(f"初始字符串: {my_str}")

# 查 - 访问字符
print(f"索引 0: {my_str[0]}")
print(f"切片 [7:13]: {my_str[7:13]}")

# 字符串不可修改，尝试修改会引发错误
# my_str[0] = 'h'  # 这会引发 TypeError

# 字符串操作
print(f"大写: {my_str.upper()}")
print(f"小写: {my_str.lower()}")
print(f"首字母大写: {my_str.capitalize()}")
print(f"每个单词首字母大写: {my_str.title()}")
print(f"替换 'Python' 为 'World': {my_str.replace('Python', 'World')}")
print(f"分割: {my_str.split(', ')}")
print(f"是否以 'Hello' 开头: {my_str.startswith('Hello')}")
print(f"是否以 '!' 结尾: {my_str.endswith('!')}")
print(f"查找 'Python': {my_str.find('Python')}")
print(f"计数 'o': {my_str.count('o')}")

# 连接字符串
str1 = "Hello"
str2 = "World"
print(f"连接字符串: {str1 + ', ' + str2 + '!'}")
print(f"使用 format(): {'{} {}, {}!'.format(str1, str2.lower(), 2023)}")
print(f"使用 f-string: {str1}, {str2.lower()}, {2023}!")

# 6. 数据结构的嵌套
print("\n6. 数据结构的嵌套")

# 嵌套列表
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"嵌套列表: {nested_list}")
print(f"访问嵌套元素: {nested_list[1][2]}")

# 嵌套字典
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(f"嵌套字典: {nested_dict}")
print(f"访问嵌套值: {nested_dict['person1']['name']}")

# 字典与列表的混合嵌套
contacts = [
    {"name": "Alice", "phone": "123-456-7890", "emails": ["alice@example.com", "a@work.com"]},
    {"name": "Bob", "phone": "987-654-3210", "emails": ["bob@example.com"]}
]
print(f"混合嵌套结构: {contacts}")
print(f"访问复杂嵌套值: {contacts[0]['emails'][1]}")

# 7. 高级数据结构操作
print("\n7. 高级数据结构操作")

# 列表推导式
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(f"列表推导式计算平方: {squares}")

even_squares = [n**2 for n in numbers if n % 2 == 0]
print(f"条件列表推导式: {even_squares}")

# 字典推导式
word_lengths = {word: len(word) for word in ["Python", "is", "awesome"]}
print(f"字典推导式: {word_lengths}")

# 集合推导式
unique_squares = {n**2 for n in [1, 2, 2, 3, 3, 3]}
print(f"集合推导式: {unique_squares}")

# 8. 数据结构的排序
print("\n8. 数据结构的排序")

# 列表排序
to_sort = [5, 2, 9, 1, 5, 6]
print(f"原始列表: {to_sort}")

to_sort.sort()
print(f"sort() 后 (原地排序): {to_sort}")

# 使用 sorted() 函数（不修改原列表）
to_sort = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(to_sort)
print(f"sorted() 后: {sorted_list}")
print(f"原列表不变: {to_sort}")

# 逆序排序
to_sort.sort(reverse=True)
print(f"逆序排序后: {to_sort}")

# 按自定义键排序
words = ["apple", "banana", "cherry", "date"]
words_sorted_by_length = sorted(words, key=len)
print(f"按长度排序的单词: {words_sorted_by_length}")

# 9. 数据结构的迭代
print("\n9. 数据结构的迭代")

# 遍历列表
fruits = ["apple", "banana", "cherry"]
print("遍历列表:")
for fruit in fruits:
    print(f"- {fruit}")

# 使用 enumerate() 遍历并获取索引
print("使用 enumerate() 遍历:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 遍历字典
person = {"name": "Alice", "age": 30, "city": "New York"}
print("遍历字典键:")
for key in person:
    print(f"- {key}")

print("遍历字典值:")
for value in person.values():
    print(f"- {value}")

print("遍历字典键值对:")
for key, value in person.items():
    print(f"- {key}: {value}")

# 10. 数据结构的复制
print("\n10. 数据结构的复制")

# 浅复制
original = [1, [2, 3], 4]
shallow_copy = original.copy()
print(f"原始列表: {original}")
print(f"浅复制: {shallow_copy}")

# 修改浅复制中的嵌套列表元素，会影响原始列表
shallow_copy[1][0] = 'X'
print(f"修改浅复制后，原始列表: {original}")
print(f"修改浅复制后，浅复制: {shallow_copy}")

# 深复制
import copy
original = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original)
print(f"\n原始列表: {original}")
print(f"深复制: {deep_copy}")

# 修改深复制中的嵌套列表元素，不会影响原始列表
deep_copy[1][0] = 'Y'
print(f"修改深复制后，原始列表: {original}")
print(f"修改深复制后，深复制: {deep_copy}")