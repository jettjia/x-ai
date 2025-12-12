#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python文件操作示例

print("Python 文件操作示例\n" + "="*50)

import os
import shutil

def create_sample_directory():
    """创建示例目录和文件"""
    if not os.path.exists('sample_files'):
        os.makedirs('sample_files')
        print("已创建示例目录: sample_files")

create_sample_directory()

# 1. 文件的基本操作
print("\n1. 文件的基本操作")

print("\n1.1 创建和写入文件")
# 写入文本文件
with open('sample_files/text_file.txt', 'w', encoding='utf-8') as f:
    f.write("这是第一行文本。\n")
    f.write("这是第二行文本。\n")
    f.write("这是包含中文的第三行文本。\n")

print("已创建文本文件: sample_files/text_file.txt")

# 追加内容到文件
with open('sample_files/text_file.txt', 'a', encoding='utf-8') as f:
    f.write("这是追加的第一行内容。\n")
    f.write("这是追加的第二行内容。\n")

print("已向文件追加内容")

# 1.2 读取文件
print("\n1.2 读取文件")

# 读取整个文件
with open('sample_files/text_file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("读取整个文件内容:")
    print(content)

# 逐行读取文件
print("\n逐行读取文件内容:")
with open('sample_files/text_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(f"行内容: {line.strip()}")

# 读取所有行到列表
with open('sample_files/text_file.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("\n读取所有行到列表:")
    print(f"文件共有 {len(lines)} 行")

# 1.3 二进制文件操作
print("\n1.3 二进制文件操作")

# 创建二进制文件
binary_data = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x20, 0x57, 0x6F, 0x72, 0x6C, 0x64])
with open('sample_files/binary_file.bin', 'wb') as f:
    f.write(binary_data)

print("已创建二进制文件: sample_files/binary_file.bin")
print(f"二进制数据: {binary_data.hex()}")

# 读取二进制文件
with open('sample_files/binary_file.bin', 'rb') as f:
    read_data = f.read()
    print(f"读取的二进制数据: {read_data.hex()}")
    print(f"转换为字符串: {read_data.decode('utf-8')}")

# 2. 文件的高级操作
print("\n2. 文件的高级操作")

# 2.1 文件指针操作
print("\n2.1 文件指针操作")

with open('sample_files/text_file.txt', 'r+', encoding='utf-8') as f:
    # 读取前10个字符
    first_10_chars = f.read(10)
    print(f"前10个字符: {first_10_chars}")
    
    # 获取当前文件指针位置
    current_position = f.tell()
    print(f"当前文件指针位置: {current_position}")
    
    # 移动文件指针到开头
    f.seek(0)
    print(f"移动文件指针到开头后，读取的内容: {f.read(5)}")
    
    # 移动文件指针到结尾
    f.seek(0, 2)  # 0是偏移量，2表示相对于文件结尾
    print(f"文件大小: {f.tell()} 字节")

# 2.2 上下文管理器和文件关闭
print("\n2.2 上下文管理器和文件关闭")
print("使用with语句会自动关闭文件，这是推荐的文件操作方式")
print("不使用with语句时，需要手动调用close()方法关闭文件")

# 不使用with语句的情况
try:
    f = open('sample_files/text_file.txt', 'r', encoding='utf-8')
    content = f.read(10)
    print(f"手动打开文件读取: {content}")
finally:
    # 确保文件被关闭
    if f and not f.closed:
        f.close()
        print("文件已手动关闭")

# 2.3 大文件处理
print("\n2.3 大文件处理")
print("处理大文件时，应避免一次性读取整个文件到内存")

# 创建一个稍大的文件用于演示
size_mb = 1  # 文件大小约为1MB
chunk_size = 1024 * 100  # 100KB

with open('sample_files/large_file.txt', 'w', encoding='utf-8') as f:
    data = 'x' * chunk_size
    for _ in range((size_mb * 1024 * 1024) // chunk_size):
        f.write(data)

print(f"已创建约 {size_mb}MB 的大文件: sample_files/large_file.txt")

# 分块读取大文件
print("\n分块读取大文件示例:")
line_count = 0
with open('sample_files/large_file.txt', 'r', encoding='utf-8') as f:
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        line_count += chunk.count('x')  # 统计'x'的数量（仅用于演示）
        # 处理当前块...

print(f"大文件中'x'的数量: {line_count}")

# 3. 文件和目录管理
print("\n3. 文件和目录管理")

# 3.1 检查文件和目录是否存在
print("\n3.1 检查文件和目录是否存在")

file_exists = os.path.exists('sample_files/text_file.txt')
dir_exists = os.path.exists('sample_files')

print(f"文件 sample_files/text_file.txt 是否存在: {file_exists}")
print(f"目录 sample_files 是否存在: {dir_exists}")
print(f"文件是否为普通文件: {os.path.isfile('sample_files/text_file.txt')}")
print(f"文件是否为目录: {os.path.isdir('sample_files')}")

# 3.2 获取文件信息
print("\n3.2 获取文件信息")

if os.path.exists('sample_files/text_file.txt'):
    file_size = os.path.getsize('sample_files/text_file.txt')
    created_time = os.path.getctime('sample_files/text_file.txt')
    modified_time = os.path.getmtime('sample_files/text_file.txt')
    access_time = os.path.getatime('sample_files/text_file.txt')
    
    print(f"文件大小: {file_size} 字节")
    print(f"创建时间: {created_time}")
    print(f"修改时间: {modified_time}")
    print(f"访问时间: {access_time}")
    
    # 将时间戳转换为可读格式
    import datetime
    print(f"格式化的修改时间: {datetime.datetime.fromtimestamp(modified_time)}")

# 3.3 文件重命名和移动
print("\n3.3 文件重命名和移动")

# 重命名文件
old_name = 'sample_files/text_file.txt'
new_name = 'sample_files/renamed_file.txt'

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"已将文件 {old_name} 重命名为 {new_name}")

# 移动文件
source = new_name
destination = 'sample_files/moved_file.txt'

if os.path.exists(source):
    shutil.move(source, destination)
    print(f"已将文件 {source} 移动到 {destination}")

# 3.4 文件复制
print("\n3.4 文件复制")

# 复制文件
src = 'sample_files/moved_file.txt'
dst = 'sample_files/copied_file.txt'

if os.path.exists(src):
    shutil.copy2(src, dst)  # copy2会保留文件的元数据
    print(f"已将文件 {src} 复制到 {dst}")

# 3.5 删除文件
print("\n3.5 删除文件")

# 删除文件
delete_file = 'sample_files/copied_file.txt'

if os.path.exists(delete_file):
    os.remove(delete_file)
    print(f"已删除文件: {delete_file}")

# 4. 目录操作
print("\n4. 目录操作")

# 4.1 创建目录
print("\n4.1 创建目录")

new_dir = 'sample_files/new_directory'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    print(f"已创建目录: {new_dir}")

# 创建嵌套目录
nested_dir = 'sample_files/level1/level2/level3'
if not os.path.exists(nested_dir):
    os.makedirs(nested_dir, exist_ok=True)  # exist_ok=True可以避免目录已存在时的错误
    print(f"已创建嵌套目录: {nested_dir}")

# 4.2 列出目录内容
print("\n4.2 列出目录内容")

print("sample_files 目录下的内容:")
for item in os.listdir('sample_files'):
    item_path = os.path.join('sample_files', item)
    if os.path.isfile(item_path):
        print(f"- 文件: {item}")
    else:
        print(f"- 目录: {item}")

# 4.3 遍历目录树
print("\n4.3 遍历目录树")

print("遍历 sample_files 目录树:")
for root, dirs, files in os.walk('sample_files'):
    level = root.replace('sample_files', '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

# 4.4 删除目录
print("\n4.4 删除目录")

# 删除空目录
dir_to_remove = 'sample_files/new_directory'
if os.path.exists(dir_to_remove) and os.path.isdir(dir_to_remove):
    os.rmdir(dir_to_remove)
    print(f"已删除空目录: {dir_to_remove}")

# 删除非空目录
nested_dir_to_remove = 'sample_files/level1'
if os.path.exists(nested_dir_to_remove) and os.path.isdir(nested_dir_to_remove):
    shutil.rmtree(nested_dir_to_remove)
    print(f"已删除非空目录树: {nested_dir_to_remove}")

# 5. 文件路径操作
print("\n5. 文件路径操作")

# 5.1 路径拼接和解析
print("\n5.1 路径拼接和解析")

# 路径拼接
dir_path = 'sample_files'
file_name = 'moved_file.txt'
full_path = os.path.join(dir_path, file_name)
print(f"拼接后的路径: {full_path}")

# 解析路径
base_dir = os.path.dirname(full_path)
file_name = os.path.basename(full_path)
extension = os.path.splitext(file_name)[1]
print(f"目录部分: {base_dir}")
print(f"文件名部分: {file_name}")
print(f"文件扩展名: {extension}")

# 获取绝对路径
abs_path = os.path.abspath(full_path)
print(f"绝对路径: {abs_path}")

# 5.2 规范化路径
print("\n5.2 规范化路径")

# 规范化路径（解决路径中的..和.）
normalized_path = os.path.normpath('sample_files/../sample_files/moved_file.txt')
print(f"规范化后的路径: {normalized_path}")

# 检查路径是否为绝对路径
is_abs = os.path.isabs('sample_files/moved_file.txt')
is_abs2 = os.path.isabs(abs_path)
print(f"'sample_files/moved_file.txt' 是绝对路径: {is_abs}")
print(f"'{abs_path}' 是绝对路径: {is_abs2}")

# 6. 实际应用案例
print("\n6. 实际应用案例")

# 6.1 文本文件处理
print("\n6.1 文本文件处理")

# 案例1: 统计文件中的单词数量
def count_words(file_path):
    """统计文件中的单词数量"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            words = content.split()
            return len(words)
    except Exception as e:
        print(f"统计单词数量时出错: {e}")
        return 0

word_count = count_words('sample_files/moved_file.txt')
print(f"文件 sample_files/moved_file.txt 中的单词数量: {word_count}")

# 案例2: 查找文件中的特定行
def find_lines(file_path, keyword):
    """查找文件中包含特定关键词的行"""
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if keyword in line:
                    results.append((line_num, line.strip()))
    except Exception as e:
        print(f"查找关键词时出错: {e}")
    return results

keyword = "中文"
found_lines = find_lines('sample_files/moved_file.txt', keyword)
print(f"文件 sample_files/moved_file.txt 中包含关键词 '{keyword}' 的行:")
for line_num, line in found_lines:
    print(f"第 {line_num} 行: {line}")

# 案例3: 合并多个文件
def merge_files(output_file, *input_files):
    """合并多个文件的内容到一个输出文件"""
    try:
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for input_file in input_files:
                if os.path.exists(input_file):
                    out_f.write(f"\n===== 开始合并文件: {input_file} =====\n")
                    with open(input_file, 'r', encoding='utf-8') as in_f:
                        out_f.write(in_f.read())
                    out_f.write(f"\n===== 结束合并文件: {input_file} =====\n")
                else:
                    print(f"文件 {input_file} 不存在，跳过")
        print(f"已将 {len(input_files)} 个文件合并到 {output_file}")
    except Exception as e:
        print(f"合并文件时出错: {e}")

# 创建另一个测试文件
with open('sample_files/another_file.txt', 'w', encoding='utf-8') as f:
    f.write("这是另一个文件的第一行。\n")
    f.write("这是另一个文件的第二行。\n")

# 合并文件
merge_files('sample_files/merged_file.txt', 'sample_files/moved_file.txt', 'sample_files/another_file.txt')

# 6.2 CSV文件处理
print("\n6.2 CSV文件处理")

import csv

# 创建CSV文件
def create_csv_file(file_path):
    """创建CSV文件"""
    data = [
        ['姓名', '年龄', '城市'],
        ['张三', 25, '北京'],
        ['李四', 30, '上海'],
        ['王五', 28, '广州'],
        ['赵六', 35, '深圳']
    ]
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    print(f"已创建CSV文件: {file_path}")

# 读取CSV文件
def read_csv_file(file_path):
    """读取CSV文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except Exception as e:
        print(f"读取CSV文件时出错: {e}")

# 使用DictReader读取CSV文件
def read_csv_with_dictreader(file_path):
    """使用DictReader读取CSV文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"姓名: {row['姓名']}, 年龄: {row['年龄']}, 城市: {row['城市']}")
    except Exception as e:
        print(f"使用DictReader读取CSV文件时出错: {e}")

# 创建并读取CSV文件
csv_file = 'sample_files/users.csv'
create_csv_file(csv_file)
print("\n使用普通reader读取CSV文件:")
read_csv_file(csv_file)
print("\n使用DictReader读取CSV文件:")
read_csv_with_dictreader(csv_file)

# 6.3 JSON文件处理
print("\n6.3 JSON文件处理")

import json

# 创建JSON文件
def create_json_file(file_path):
    """创建JSON文件"""
    data = {
        'name': '张三',
        'age': 25,
        'city': '北京',
        'hobbies': ['阅读', '旅游', '编程'],
        'education': {
            'degree': '本科',
            'major': '计算机科学',
            'university': '北京大学'
        },
        'is_student': False
    }
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"已创建JSON文件: {file_path}")

# 读取JSON文件
def read_json_file(file_path):
    """读取JSON文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"姓名: {data['name']}")
            print(f"年龄: {data['age']}")
            print(f"城市: {data['city']}")
            print(f"爱好: {', '.join(data['hobbies'])}")
            print(f"教育: {data['education']['degree']}, {data['education']['major']}, {data['education']['university']}")
            print(f"是否学生: {data['is_student']}")
    except Exception as e:
        print(f"读取JSON文件时出错: {e}")

# 创建并读取JSON文件
json_file = 'sample_files/user_info.json'
create_json_file(json_file)
print("\n读取JSON文件内容:")
read_json_file(json_file)

# 7. 文件操作的最佳实践
print("\n7. 文件操作的最佳实践")
print("- 始终使用with语句来打开文件，确保文件正确关闭")
print("- 指定文件编码，特别是处理非ASCII字符时")
print("- 处理文件操作可能出现的异常")
print("- 避免一次性读取大文件到内存")
print("- 使用os.path模块进行路径操作，确保跨平台兼容性")
print("- 对于CSV、JSON等结构化数据，使用专门的模块处理")
print("- 在操作文件前检查文件或目录是否存在")
print("- 使用二进制模式处理二进制文件")
print("- 注意文件权限问题")

print("\n总结：")
print("Python提供了丰富的文件操作功能，可以满足各种文件读写需求")
print("合理使用这些功能可以高效地处理文件数据")
print("在实际项目中，应根据具体需求选择合适的文件操作方式")
print("并且始终遵循最佳实践，确保代码的健壮性和可维护性")