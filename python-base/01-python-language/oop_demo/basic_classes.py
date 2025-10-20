#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"基本类定义模块"

class Person:
    """Person 类 - 演示基本的面向对象概念"""
    
    # 类变量（所有实例共享）
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age, gender):
        """构造函数 - 初始化实例变量"""
        # 实例变量（每个实例独有）
        self.name = name
        self.age = age
        self.gender = gender
        # 访问并修改类变量
        Person.population += 1
    
    # 实例方法 - 访问实例变量和类变量
    def greet(self):
        """实例方法，打招呼"""
        return f"Hello, my name is {self.name}."
    
    # 实例方法可以修改实例变量
    def celebrate_birthday(self):
        """庆祝生日，增加年龄"""
        self.age += 1
        return f"Happy Birthday, {self.name}! You are now {self.age} years old."
    
    # 类方法 - 使用 @classmethod 装饰器
    @classmethod
    def get_species(cls):
        """类方法，返回物种信息"""
        return f"This class represents {cls.species}."
    
    @classmethod
    def get_population(cls):
        """类方法，返回人口数量"""
        return f"Current population: {cls.population}."
    
    # 静态方法 - 使用 @staticmethod 装饰器
    @staticmethod
    def is_adult(age):
        """静态方法，判断是否成年"""
        return age >= 18

# 继承示例
class Student(Person):
    """Student 类 - 继承自 Person 类"""
    
    def __init__(self, name, age, gender, student_id, major):
        """构造函数，调用父类构造函数并添加新的实例变量"""
        # 调用父类的构造函数
        super().__init__(name, age, gender)
        # 添加子类特有的实例变量
        self.student_id = student_id
        self.major = major
        self.grades = {}
    
    # 重写父类的方法
    def greet(self):
        """重写父类的 greet 方法"""
        base_greeting = super().greet()
        return f"{base_greeting} I'm a student majoring in {self.major}."
    
    # 添加子类特有的方法
    def add_grade(self, course, grade):
        """添加课程成绩"""
        self.grades[course] = grade
        return f"Added grade {grade} for course {course}."
    
    def get_gpa(self):
        """计算平均成绩"""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades.values())