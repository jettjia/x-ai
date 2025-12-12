#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""面向对象编程演示文件

这个文件展示了Python中面向对象编程的核心概念，包括:
1. 类和对象的创建
2. 实例变量和类变量
3. 实例方法、类方法和静态方法
4. 继承和多态
5. 魔法方法的使用

所有示例基于 oop_demo 包中的类定义。
"""

# 导入必要的类
from oop_demo import Person, Student, Vehicle, Car, ElectricCar, Vector, Book

# 1. 类和对象创建
print("="*60)
print("1. 类和对象创建")
print("="*60)

# 创建对象（实例化）
person1 = Person("Alice", 30, "Female")
person2 = Person("Bob", 25, "Male")

# 访问实例变量
print(f"person1.name: {person1.name}")
print(f"person1.age: {person1.age}")
print(f"person2.name: {person2.name}")
print(f"person2.age: {person2.age}")

# 类变量在所有实例之间共享
print(f"更新后的 Person.population: {Person.population}")

# 通过实例访问类变量
print(f"person1.species: {person1.species}")
print(f"person2.species: {person2.species}")

# 修改类变量（会影响所有实例）
Person.species = "Homo sapiens sapiens"
print(f"修改后的 Person.species: {Person.species}")
print(f"person1.species: {person1.species}")
print(f"person2.species: {person2.species}")

print("\n")

# 2. 实例方法、类方法和静态方法
print("="*60)
print("2. 实例方法、类方法和静态方法")
print("="*60)

# 调用实例方法
print(f"person1.greet(): {person1.greet()}")
print(f"person1.celebrate_birthday(): {person1.celebrate_birthday()}")
print(f"person1.age 现在为: {person1.age}")

# 调用类方法（通过类或实例调用）
print(f"Person.get_species(): {Person.get_species()}")
print(f"person1.get_species(): {person1.get_species()}")
print(f"Person.get_population(): {Person.get_population()}")

# 调用静态方法（通过类或实例调用）
print(f"Person.is_adult(18): {Person.is_adult(18)}")
print(f"Person.is_adult(16): {Person.is_adult(16)}")
print(f"person1.is_adult(20): {person1.is_adult(20)}")

print("\n")

# 3. 继承
print("="*60)
print("3. 继承")
print("="*60)

# 创建子类实例
student1 = Student("Charlie", 20, "Male", "S12345", "Computer Science")

# 访问继承的属性和方法
print(f"student1.name: {student1.name}")
print(f"student1.greet(): {student1.greet()}")  # 重写的方法
print(f"student1.celebrate_birthday(): {student1.celebrate_birthday()}")  # 继承的方法

# 调用子类特有的方法
print(f"student1.add_grade('Math', 90): {student1.add_grade('Math', 90)}")
print(f"student1.add_grade('Physics', 85): {student1.add_grade('Physics', 85)}")
print(f"student1.get_gpa(): {student1.get_gpa():.2f}")

print("\n")

# 4. 多级继承
print("="*60)
print("4. 多级继承")
print("="*60)

# 创建不同类的实例
car = Car("Toyota", "Corolla", 2020, "gasoline", 50)
electric_car = ElectricCar("Tesla", "Model 3", 2022, 75)

# 调用基类方法
print(f"car.start(): {car.start()}")
print(f"electric_car.start(): {electric_car.start()}")

# 调用重写的方法
print(f"car.refuel(): {car.refuel()}")
print(f"electric_car.refuel(): {electric_car.refuel()}")

# 调用继承的方法
print(f"car.get_fuel_status(): {car.get_fuel_status()}")
print(f"electric_car.get_fuel_status(): {electric_car.get_fuel_status()}")

# 调用子类特有的方法
print(f"electric_car.regenerative_braking(): {electric_car.regenerative_braking()}")
print(f"electric_car.get_fuel_status(): {electric_car.get_fuel_status()}")

print("\n")

# 5. 多态
print("="*60)
print("5. 多态")
print("="*60)

def vehicle_info(vehicle):
    """多态演示函数 - 接受任何 Vehicle 类型的对象"""
    print(f"Brand: {vehicle.brand}")
    print(f"Model: {vehicle.model}")
    print(f"Start: {vehicle.start()}")
    print(f"Refuel: {vehicle.refuel()}")
    print(f"Status: {vehicle.get_fuel_status()}")
    print("-")

# 传递不同类型的对象，但调用相同的方法
print("Car info:")
vehicle_info(car)
print("ElectricCar info:")
vehicle_info(electric_car)

print("\n")

# 6. 魔法方法
print("="*60)
print("6. 魔法方法")
print("="*60)

# 字符串表示魔法方法
vector = Vector(3, 4)
print(f"str(vector): {str(vector)}")  # __str__
print(f"repr(vector): {repr(vector)}")  # __repr__

# 运算符重载魔法方法
vector2 = Vector(1, 2)
print(f"vector + vector2: {vector + vector2}")  # __add__
print(f"vector - vector2: {vector - vector2}")  # __sub__
print(f"vector * 2: {vector * 2}")  # __mul__

# 比较运算符魔法方法
print(f"vector == vector2: {vector == vector2}")  # __eq__
print(f"vector < vector2: {vector < vector2}")  # __lt__

# 容器相关魔法方法
print(f"len(vector): {len(vector)}")  # __len__
print(f"vector[0]: {vector[0]}")  # __getitem__
vector[0] = 5  # __setitem__
print(f"修改后的 vector[0]: {vector[0]}")

# 其他魔法方法
print(f"abs(vector): {abs(vector)}")  # __abs__
print(f"bool(vector): {bool(vector)}")  # __bool__
print(f"vector(3): {vector(3)}")  # __call__

# 上下文管理器魔法方法
print("\n上下文管理器示例:")
with Book("Python Basics", "John Smith", 300) as my_book:
    print(f"Reading {my_book}")

# 迭代器魔法方法
print("\n迭代器示例 (只显示前5页):")
book = Book("Python Advanced", "Jane Doe", 500)
page_count = 0
for page in book:
    print(page)
    page_count += 1
    if page_count >= 5:
        break

print("\n")

# 7. 面向对象编程的最佳实践
print("="*60)
print("7. 面向对象编程的最佳实践")
print("="*60)

print("面向对象编程的最佳实践:")
print("1. 封装：将数据和行为封装在类中")
print("2. 继承：避免代码重复，扩展现有功能")
print("3. 多态：允许不同类的对象对相同的方法做出不同的响应")
print("4. 抽象：隐藏复杂实现细节，提供简单接口")
print("5. 单一职责原则：一个类应该只有一个职责")
print("6. 开闭原则：对扩展开放，对修改关闭")
print("7. 里氏替换原则：子类应该能替换父类而不改变程序行为")
print("8. 依赖倒置原则：依赖抽象，不依赖具体实现")
print("9. 接口隔离原则：不强迫客户端依赖于它们不需要的接口")
print("10. 使用文档字符串为类和方法提供文档")