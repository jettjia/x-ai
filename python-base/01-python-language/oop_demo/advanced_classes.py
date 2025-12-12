#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""高级类定义模块 - 演示多级继承和抽象概念"""

class Vehicle:
    """Vehicle 类 - 所有交通工具的基类"""
    
    def __init__(self, brand, model, year):
        """构造函数 - 初始化车辆基本信息"""
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        """启动车辆"""
        self.is_running = True
        return f"{self.brand} {self.model} started."
    
    def stop(self):
        """停止车辆"""
        self.is_running = False
        return f"{self.brand} {self.model} stopped."
    
    def refuel(self):
        """加油方法（在子类中可以被重写）"""
        return "Refueling method to be implemented in subclass."
    
    def get_fuel_status(self):
        """获取燃油状态"""
        return "Fuel status method to be implemented in subclass."

# 继承自 Vehicle 类
class Car(Vehicle):
    """Car 类 - 继承自 Vehicle 类"""
    
    def __init__(self, brand, model, year, fuel_type, fuel_capacity):
        """构造函数，调用父类构造函数并添加新的实例变量"""
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity * 0.5  # 默认油箱半满
    
    # 重写父类的方法
    def refuel(self):
        """重写父类的 refuel 方法"""
        if self.is_running:
            return "Cannot refuel while the car is running."
        self.fuel_level = self.fuel_capacity
        return f"{self.brand} {self.model} refueled with {self.fuel_type}."
    
    def get_fuel_status(self):
        """重写父类的 get_fuel_status 方法"""
        percentage = (self.fuel_level / self.fuel_capacity) * 100
        return f"Fuel level: {self.fuel_level:.1f}/{self.fuel_capacity} ({percentage:.1f}%)"

# 多级继承 - 继承自 Car 类
class ElectricCar(Car):
    """ElectricCar 类 - 多级继承示例"""
    
    def __init__(self, brand, model, year, battery_capacity):
        """构造函数，调用父类构造函数并使用电动车特定值"""
        super().__init__(brand, model, year, "electricity", battery_capacity)
        self.battery_capacity = battery_capacity
        self.charge_level = battery_capacity * 0.6  # 默认电池60%电量
    
    # 再次重写 refuel 方法以适应电动车
    def refuel(self):
        """重写 refuel 方法为充电"""
        if self.is_running:
            return "Cannot charge while the car is running."
        self.charge_level = self.battery_capacity
        return f"{self.brand} {self.model} fully charged."
    
    def get_fuel_status(self):
        """重写 get_fuel_status 方法以显示电量"""
        percentage = (self.charge_level / self.battery_capacity) * 100
        return f"Battery charge: {self.charge_level:.1f}kWh/{self.battery_capacity}kWh ({percentage:.1f}%)"
    
    # 添加电动车特有的方法
    def regenerative_braking(self):
        """电动车特有的再生制动功能"""
        if self.is_running:
            # 模拟再生制动充电
            charge_gained = min(0.1 * self.battery_capacity, self.battery_capacity - self.charge_level)
            self.charge_level += charge_gained
            return f"Regenerative braking engaged. Battery charged by {charge_gained:.1f}kWh."
        return "Cannot engage regenerative braking while the car is stopped."