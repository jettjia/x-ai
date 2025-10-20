#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""项目安装配置文件

使用setuptools配置项目的安装信息。
"""
from setuptools import setup, find_packages


# 读取README.md文件内容用于long_description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    # 项目名称
    name='project_template',
    # 项目版本
    version='0.1.0',
    # 项目描述
    description='A Python project template',
    # 详细描述（从README.md读取）
    long_description=long_description,
    long_description_content_type='text/markdown',
    # 项目URL（示例URL）
    url='https://github.com/username/project_template',
    # 作者信息
    author='Your Name',
    author_email='your.email@example.com',
    # 许可证
    license='MIT',
    # 项目分类
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    # 搜索包的目录
    packages=find_packages('src'),
    # 指定包的根目录
    package_dir={'': 'src'},
    # 项目依赖
    install_requires=[
        # 这里列出项目依赖，例如：
        # 'requests>=2.25.1',
        # 'numpy>=1.21.0',
    ],
    # 开发依赖
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.12',
            'flake8>=4.0',
        ],
    },
    # 入口点（命令行工具）
    entry_points={
        'console_scripts': [
            'project_template=project_template.main:hello_world',
        ],
    },
    # 包含的额外文件
    include_package_data=True,
    # Python版本要求
    python_requires='>=3.6',
)