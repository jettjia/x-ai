#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块与包示例演示
# 文件内容在 sample_package 目录下

print("Python 模块与包示例\n" + "="*50)

# 1. 导入标准库模块
print("\n1. 导入标准库模块")

import math
import random
import datetime

print(f"math.pi: {math.pi}")
print(f"math.sqrt(16): {math.sqrt(16)}")
print(f"random.randint(1, 10): {random.randint(1, 10)}")
print(f"当前时间: {datetime.datetime.now()}")

# 2. 导入第三方库（如果已安装）
print("\n2. 导入第三方库")

try:
    import numpy
    print(f"成功导入 numpy，版本: {numpy.__version__}")
except ImportError:
    print("numpy 未安装，可以使用 'pip install numpy' 安装")

# 3. 导入自定义模块和包
print("\n3. 导入自定义模块和包")

# 导入整个包
import sample_package
print(f"sample_package.greeting: {sample_package.greeting}")
print(f"sample_package.package_function(): {sample_package.package_function()}")

# 导入包中的模块
import sample_package.module1
print(f"sample_package.module1.module1_var: {sample_package.module1.module1_var}")
print(f"sample_package.module1.function1(): {sample_package.module1.function1()}")

# 创建模块中类的实例
instance = sample_package.module1.Class1("Test Instance")
print(f"instance.get_name(): {instance.get_name()}")

# 4. 从模块中导入特定功能
print("\n4. 从模块中导入特定功能")

from sample_package.module1 import function1, Class1, module1_var
print(f"直接使用 function1(): {function1()}")
print(f"直接使用 module1_var: {module1_var}")

# 5. 使用别名导入
print("\n5. 使用别名导入")

import sample_package.module1 as m1
print(f"使用别名 m1.function1(): {m1.function1()}")

from sample_package.module2 import function2 as f2
print(f"使用别名 f2(): {f2()}")

# 6. 导入子包和子模块
print("\n6. 导入子包和子模块")

from sample_package.subpackage import submodule
print(f"submodule.submodule_function(): {submodule.submodule_function()}")
print(f"submodule.use_parent_modules(): {submodule.use_parent_modules()}")

# 7. 相对导入的演示
print("\n7. 相对导入的演示")

print("相对导入是指在包内使用点表示法导入同一包中的其他模块或子包。")
print("- '.' 表示当前包目录")
print("- '..' 表示父包目录")
print("- '...' 表示祖父包目录，以此类推")

print("\n示例：")
print("在 module2.py 中我们使用了: from . import module1")
print("这表示从当前包（sample_package）导入 module1 模块")
print("\n在 submodule.py 中我们使用了: from .. import module1")
print("这表示从父包（sample_package）导入 module1 模块")

# 8. __import__() 函数动态导入
print("\n8. __import__() 函数动态导入")

# 使用 __import__() 函数动态导入模块
module_name = "sample_package.module1"
module = __import__(module_name)

# 注意：对于包，__import__ 返回的是顶层包
# 需要进一步获取子模块
if hasattr(module, 'module1'):
    module1 = module.module1
    print(f"动态导入 module1.function1(): {module1.function1()}")

# 使用 importlib 模块进行更灵活的动态导入
import importlib

try:
    module2 = importlib.import_module("sample_package.module2")
    print(f"使用 importlib 导入 module2.function2(): {module2.function2()}")
    print(f"使用 importlib 导入 module2.use_module1(): {module2.use_module1()}")
except ImportError as e:
    print(f"动态导入失败: {e}")

# 9. 模块搜索路径
print("\n9. 模块搜索路径")

import sys
print("Python 解释器在导入模块时会按照以下顺序搜索:")
print("1. 当前目录")
print("2. PYTHONPATH 环境变量中列出的目录")
print("3. Python 标准库目录")
print("4. 任何 .pth 文件中列出的目录")

print("\n当前的模块搜索路径 (sys.path):")
for path in sys.path:
    print(f"- {path}")

# 10. 包的 __all__ 属性
print("\n10. 包的 __all__ 属性")

print("__all__ 是一个列表，定义了当使用 'from package import *' 时会导入的模块名称")
print("在 sample_package/__init__.py 中我们定义了 __all__ = ['module1', 'module2', 'greeting', 'package_function']")

# 11. 重新加载模块
print("\n11. 重新加载模块")

# 使用 importlib.reload() 重新加载已导入的模块
importlib.reload(sample_package)
print(f"重新加载后 sample_package.greeting: {sample_package.greeting}")

# 12. 查看模块的属性和方法
print("\n12. 查看模块的属性和方法")

print(f"sample_package 模块的属性和方法:")
for attr in dir(sample_package):
    if not attr.startswith("__"):  # 过滤掉内置属性
        print(f"- {attr}")

# 13. 模块的 __file__ 和 __name__ 属性
print("\n13. 模块的 __file__ 和 __name__ 属性")

print(f"math 模块的名称: {math.__name__}")
# 检查模块是否有 __file__ 属性
if hasattr(math, '__file__'):
    print(f"math 模块的文件路径: {math.__file__}")
else:
    print("math 模块是内置模块，没有 __file__ 属性")
print(f"当前模块的名称: {__name__}")  # 通常是 "__main__"

# 14. 如何获取所有第三方库
print("\n14. 如何获取所有第三方库")

print("获取已安装的第三方库的方法:")
print("1. 使用 pip list 命令在终端查看")
print("2. 使用 pip freeze 命令生成 requirements.txt 文件")
print("3. 在代码中使用 pkg_resources 模块")

# 示例：使用 pkg_resources 列出已安装的包
try:
    import pkg_resources
    print("\n已安装的部分包:")
    # 只显示前5个包
    for i, dist in enumerate(pkg_resources.working_set):
        print(f"- {dist.project_name} ({dist.version})")
        if i >= 4:
            break
    print("...")
except ImportError:
    print("pkg_resources 模块不可用")

# 15. 模块和包的最佳实践
print("\n15. 模块和包的最佳实践")

print("模块和包的最佳实践:")
print("1. 使用清晰、描述性的名称命名模块和包")
print("2. 为模块和函数添加文档字符串")
print("3. 将相关功能组织到同一个模块或包中")
print("4. 使用相对导入在包内导入模块")
print("5. 定义 __all__ 属性控制 'import *' 的行为")
print("6. 避免模块级别有副作用的代码（除非是必要的初始化）")
print('7. 将主程序逻辑放在 "if __name__ == "__main__":" 块中')
print("8. 使用虚拟环境隔离项目依赖")