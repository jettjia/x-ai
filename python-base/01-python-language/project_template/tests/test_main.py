#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试主模块

测试main.py中的函数功能。
"""
import unittest
import os
import shutil
from project_template.main import hello_world, create_project_structure


class TestMain(unittest.TestCase):
    """测试main模块中的函数"""
    
    def test_hello_world(self):
        """测试hello_world函数的返回值"""
        result = hello_world()
        self.assertEqual(result, "Hello, World!")
        self.assertIsInstance(result, str)
        
    def test_create_project_structure(self):
        """测试create_project_structure函数是否正确创建项目结构"""
        # 定义测试项目名称和临时目录
        test_project_name = "test_project"
        test_base_dir = os.path.join(os.path.dirname(__file__), "test_temp")
        
        # 确保测试目录为空
        if os.path.exists(test_base_dir):
            shutil.rmtree(test_base_dir)
        os.makedirs(test_base_dir)
        
        try:
            # 调用函数创建项目结构
            project_path = create_project_structure(test_project_name, test_base_dir)
            
            # 验证项目路径是否正确
            expected_path = os.path.join(test_base_dir, test_project_name)
            self.assertEqual(project_path, expected_path)
            
            # 验证主要目录是否存在
            self.assertTrue(os.path.exists(os.path.join(project_path, "src")))
            self.assertTrue(os.path.exists(os.path.join(project_path, "src", test_project_name)))
            self.assertTrue(os.path.exists(os.path.join(project_path, "tests")))
            self.assertTrue(os.path.exists(os.path.join(project_path, "data")))
            self.assertTrue(os.path.exists(os.path.join(project_path, "docs")))
            
            # 验证主要文件是否存在
            self.assertTrue(os.path.exists(os.path.join(project_path, "setup.py")))
            self.assertTrue(os.path.exists(os.path.join(project_path, "requirements.txt")))
            self.assertTrue(os.path.exists(os.path.join(project_path, "README.md")))
            self.assertTrue(os.path.exists(os.path.join(project_path, ".gitignore")))
        finally:
            # 清理测试目录
            if os.path.exists(test_base_dir):
                shutil.rmtree(test_base_dir)


if __name__ == '__main__':
    unittest.main()