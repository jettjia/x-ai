#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第三方库示例

print("Python 第三方库示例\n" + "="*50)

# 1. 如何导入第三方库
print("\n1. 如何导入第三方库")

print("在Python中，导入第三方库非常简单，使用import语句即可。例如：")
print("import numpy")
print("import pandas as pd  # 使用别名")
print("from matplotlib import pyplot as plt  # 从库中导入特定模块")

print("\n第三方库通常需要先安装，使用pip工具进行安装。")
print("例如：pip install numpy pandas matplotlib")

# 2. 在哪里能获取到所有第三方库
print("\n2. 在哪里能获取到所有第三方库")

print("获取第三方库的主要途径：")
print("1. PyPI (Python Package Index): https://pypi.org/")
print("   - 官方的Python包仓库，包含超过30万个包")
print("   - 可以通过网站搜索，或使用pip search命令(新版pip已移除)")
print("2. Anaconda: https://anaconda.org/")
print("   - 科学计算领域常用的发行版，包含1500多个预安装的包")
print("3. GitHub: https://github.com/")
print("   - 许多开源库的托管平台，可以找到最新的开发版本")
print("4. 官方文档和教程")
print("5. 社区推荐和博客文章")

# 3. 导入matplotlib并编写一个简单案例
print("\n3. 导入matplotlib并编写一个简单案例")

try:
    # 导入matplotlib的pyplot模块
    import matplotlib.pyplot as plt
    
    print("成功导入matplotlib库")
    
    # 创建数据
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    squares = [1, 4, 9, 16, 25]
    
    # 创建一个图形
    plt.figure(figsize=(10, 6))
    
    # 绘制折线图
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='线性关系')
    plt.plot(x, squares, marker='s', linestyle='--', color='r', label='平方关系')
    
    # 添加标题和标签
    plt.title('简单折线图示例', fontsize=15)
    plt.xlabel('X轴', fontsize=12)
    plt.ylabel('Y轴', fontsize=12)
    
    # 添加图例
    plt.legend()
    
    # 添加网格
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 设置坐标轴范围
    plt.xlim(0, 6)
    plt.ylim(0, 30)
    
    # 保存图形
    plt.savefig('/home/jett/c/x-embedded/03-python-language/simple_plot.png')
    print("图形已保存为 'simple_plot.png'")
    
    # 显示图形
    print("如果在图形界面环境中运行，将显示图形")
    # plt.show()  # 注释掉，避免在非图形环境中运行出错
    
    # 创建一个饼图示例
    plt.figure(figsize=(8, 8))
    labels = ['A', 'B', 'C', 'D']
    sizes = [30, 25, 20, 25]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    explode = (0.1, 0, 0, 0)  # 突出显示第一个部分
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # 确保饼图是圆的
    plt.title('简单饼图示例', fontsize=15)
    
    # 保存饼图
    plt.savefig('/home/jett/c/x-embedded/03-python-language/pie_chart.png')
    print("饼图已保存为 'pie_chart.png'")
    
    # 创建一个柱状图示例
    plt.figure(figsize=(10, 6))
    categories = ['类别1', '类别2', '类别3', '类别4']
    values = [12, 19, 15, 25]
    
    plt.bar(categories, values, color='skyblue')
    plt.title('简单柱状图示例', fontsize=15)
    plt.xlabel('类别', fontsize=12)
    plt.ylabel('数值', fontsize=12)
    
    # 在柱子上显示数值
    for i, v in enumerate(values):
        plt.text(i, v + 0.5, str(v), ha='center')
    
    # 保存柱状图
    plt.savefig('/home/jett/c/x-embedded/03-python-language/bar_chart.png')
    print("柱状图已保存为 'bar_chart.png'")
    
    print("\nmatplotlib简单案例演示完成！")
    
except ImportError:
    print("错误: 未安装matplotlib库。")
    print("请在终端中运行以下命令安装:")
    print("pip install matplotlib")
    print("\n如果遇到权限问题，可以使用:")
    print("pip install --user matplotlib")
    print("\n或者使用虚拟环境:")
    print("python -m venv myenv")
    print("source myenv/bin/activate  # 在Windows上使用: myenv\\Scripts\\activate")
    print("pip install matplotlib")

# 4. pip常见的使用方法
print("\n4. pip常见的使用方法")

print("pip是Python的包管理器，用于安装和管理第三方库。")
print("以下是pip的一些常用命令:")

print("\n安装包:")
print("pip install package_name         # 安装指定的包")
print("pip install package_name==1.0.0  # 安装指定版本的包")
print("pip install 'package_name>=1.0.0' # 安装不低于指定版本的包")
print("pip install -r requirements.txt  # 从requirements.txt文件安装包")

print("\n升级包:")
print("pip install --upgrade package_name  # 升级指定的包")
print("pip install --upgrade pip           # 升级pip本身")

print("\n卸载包:")
print("pip uninstall package_name  # 卸载指定的包")

print("\n列出已安装的包:")
print("pip list                    # 列出所有已安装的包")
print("pip list --outdated         # 列出所有需要升级的包")

print("\n显示包的信息:")
print("pip show package_name       # 显示指定包的详细信息")

print("\n搜索包:")
print("注意: 新版pip已移除search命令，可以使用PyPI网站搜索")
print("https://pypi.org/search/")

print("\n生成requirements.txt文件:")
print("pip freeze > requirements.txt  # 将当前环境的所有包及其版本保存到文件")

print("\n从requirements.txt安装:")
print("pip install -r requirements.txt  # 安装文件中列出的所有包")

print("\n指定安装源:")
print("pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple  # 使用清华镜像源")
print("\n常用的国内镜像源:")
print("- 清华: https://pypi.tuna.tsinghua.edu.cn/simple")
print("- 阿里云: https://mirrors.aliyun.com/pypi/simple/")
print("- 豆瓣: https://pypi.douban.com/simple/")
print("- 中科大: https://pypi.mirrors.ustc.edu.cn/simple/")

print("\n设置默认镜像源:")
print("可以通过配置pip.conf文件来设置默认镜像源，避免每次都要指定。")

print("\npip的高级用法:")
print("pip check                      # 检查已安装包的依赖问题")
print("pip cache dir                  # 显示pip缓存目录")
print("pip cache purge                # 清空pip缓存")
print("pip install --no-cache-dir package_name  # 不使用缓存安装包")
print("pip wheel package_name         # 为包创建wheel文件")

# 5. 其他常用第三方库简介
print("\n5. 其他常用第三方库简介")

print("Python有大量的第三方库，以下是一些常用的库:")

print("\n数据科学和分析:")
print("- NumPy: 用于数值计算的基础库，提供多维数组支持")
print("- Pandas: 提供高性能、易用的数据结构和数据分析工具")
print("- Matplotlib: 绘图库，用于创建各种静态、动态、交互式图表")
print("- Seaborn: 基于matplotlib的统计数据可视化库")
print("- Scipy: 科学计算库，提供统计、优化、积分等功能")
print("- Scikit-learn: 机器学习库，提供各种分类、回归、聚类算法")

print("\nWeb开发:")
print("- Django: 高级Web框架，提供完整的Web开发解决方案")
print("- Flask: 轻量级Web框架，灵活且易于扩展")
print("- FastAPI: 现代、快速的Web框架，基于Python类型提示")
print("- Requests: 简洁而优雅的HTTP库")

print("\n自动化和爬虫:")
print("- Selenium: 用于Web应用程序测试的工具，也可用于爬虫")
print("- BeautifulSoup: 用于从HTML和XML文件中提取数据")
print("- Scrapy: 强大的Web爬虫框架")
print("- PyAutoGUI: 用于自动化GUI交互")

print("\n数据库:")
print("- SQLAlchemy: SQL工具包和对象关系映射器")
print("- Psycopg2: PostgreSQL数据库适配器")
print("- PyMySQL: MySQL数据库适配器")
print("- sqlite3: Python标准库中的SQLite接口")

print("\nGUI开发:")
print("- Tkinter: Python标准库中的GUI工具包")
print("- PyQt/PySide: Python绑定Qt库，功能强大的GUI开发工具")
print("- Kivy: 开源Python库，用于开发多点触控应用")

print("\n其他实用库:")
print("- TensorFlow/PyTorch: 深度学习框架")
print("- OpenCV: 计算机视觉库")
print("- Pygame: 游戏开发库")
print("- Pillow: Python图像处理库")
print("- pytest: 单元测试框架")
print("- logging: Python标准库中的日志模块")

# 6. 第三方库的最佳实践
print("\n6. 第三方库的最佳实践")

print("使用第三方库的最佳实践:")
print("1. 始终使用虚拟环境来隔离项目依赖")
print("2. 为每个项目创建requirements.txt文件")
print("3. 明确指定依赖包的版本，避免兼容性问题")
print("4. 定期更新依赖包，并测试兼容性")
print("5. 只安装项目实际需要的库")
print("6. 阅读并理解第三方库的许可协议")
print("7. 优先使用官方文档和示例")
print("8. 注意第三方库的维护状态和社区活跃度")
print("9. 在生产环境中，考虑依赖包的安全性")
print("10. 对于关键业务，考虑代码审查和测试覆盖")