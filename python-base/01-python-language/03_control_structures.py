#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 控制结构示例

print("Python 控制结构示例\n" + "="*50)

# 1. if 条件语句
print("\n1. if 条件语句")
x = 10

if x > 0:
    print(f"{x} 是正数")
elif x < 0:
    print(f"{x} 是负数")
else:
    print(f"{x} 是零")

# 2. 嵌套 if 语句
print("\n2. 嵌套 if 语句")
number = 15

if number % 2 == 0:
    print(f"{number} 是偶数")
    if number % 4 == 0:
        print(f"{number} 也是4的倍数")
else:
    print(f"{number} 是奇数")
    if number % 3 == 0:
        print(f"{number} 也是3的倍数")

# 3. while 循环
print("\n3. while 循环")
count = 0
while count < 5:
    print(f"while 循环, 计数: {count}")
    count += 1

# 4. for 循环 - 循环10次
print("\n4. for 循环 - 循环10次")
for i in range(10):
    print(f"for 循环第 {i+1} 次")

# 5. range() 函数的不同用法
print("\n5. range() 函数的不同用法")

# range(stop) - 从0开始到stop-1
print("range(5):", list(range(5)))

# range(start, stop) - 从start开始到stop-1
print("range(2, 8):", list(range(2, 8)))

# range(start, stop, step) - 带步长
print("range(1, 10, 2):", list(range(1, 10, 2)))

# 负数步长
print("range(10, 0, -2):", list(range(10, 0, -2)))

# 6. for 循环遍历列表
print("\n6. for 循环遍历列表")
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
for fruit in fruits:
    print(f"水果: {fruit}")

# 7. 使用 enumerate() 获取索引和值
print("\n7. 使用 enumerate() 获取索引和值")
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 8. 循环嵌套
print("\n8. 循环嵌套")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # 换行

# 9. break 语句 - 跳出循环
print("\n9. break 语句")
for i in range(100):
    if i == 5:
        print(f"找到数字 {i}，跳出循环")
        break
    print(f"当前数字: {i}")

# 10. continue 语句 - 跳过当前循环
print("\n10. continue 语句")
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(f"奇数: {i}")

# 11. else 子句与循环结合
print("\n11. else 子句与循环结合")

# for-else
print("寻找数字 7:")
for i in range(5):
    print(f"检查 {i}")
    if i == 7:
        print("找到数字 7")
        break
else:
    print("没有找到数字 7")

# while-else
count = 0
print("\n尝试 3 次:")
while count < 3:
    print(f"尝试 {count+1}")
    count += 1
else:
    print("完成所有尝试")

# 12. pass 语句 - 空语句
print("\n12. pass 语句")
for i in range(3):
    pass  # 占位符，什么都不做
print("pass 语句执行完毕")

# 13. 列表推导式 - 更简洁的循环方式
print("\n13. 列表推导式")
# 生成0-9的平方列表
squares = [i*i for i in range(10)]
print(f"0-9的平方: {squares}")

# 带条件的列表推导式 - 生成0-9的偶数平方
even_squares = [i*i for i in range(10) if i % 2 == 0]
print(f"0-9的偶数平方: {even_squares}")

# 嵌套列表推导式 - 转置矩阵
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f"原矩阵: {matrix}")
print(f"转置后: {transposed}")

# 14. 字典推导式
print("\n14. 字典推导式")
# 创建数字到其平方的映射
square_dict = {i: i*i for i in range(5)}
print(f"数字到平方的映射: {square_dict}")

# 15. 集合推导式
print("\n15. 集合推导式")
# 创建包含0-9平方的集合
square_set = {i*i for i in range(5)}
print(f"平方集合: {square_set}")

# 16. 生成器表达式
print("\n16. 生成器表达式")
# 创建一个生成器，而不是立即计算所有值
square_gen = (i*i for i in range(1000))
print(f"生成器对象: {square_gen}")
print(f"生成器的前5个值: {[next(square_gen) for _ in range(5)]}")

# 17. match 语句（Python 3.10+）
print("\n17. match 语句")
value = "apple"

match value:
    case "apple":
        print("这是一个苹果")
    case "banana":
        print("这是一个香蕉")
    case "orange" | "grape":
        print("这是柑橘类或葡萄")
    case _:
        print("未知水果")

# 18. 高级循环技巧
print("\n18. 高级循环技巧")

# 同时遍历两个列表
names = ["张三", "李四", "王五"]
ages = [25, 30, 35]
print("使用 zip() 同时遍历两个列表:")
for name, age in zip(names, ages):
    print(f"{name}: {age}岁")

# 反向遍历
print("\n反向遍历列表:")
for fruit in reversed(fruits):
    print(fruit)

# 排序后遍历
print("\n排序后遍历列表:")
for fruit in sorted(fruits):
    print(fruit)

# 排序并保持原列表不变
print(f"\n原列表: {fruits}")
sorted_fruits = sorted(fruits)
print(f"排序后列表: {sorted_fruits}")
print(f"原列表仍为: {fruits}")

# 使用 sorted() 的 key 参数
print("\n按长度排序:")
for fruit in sorted(fruits, key=len):
    print(fruit)