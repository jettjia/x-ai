#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python多线程编程示例

print("Python 多线程编程示例\n" + "="*50)

# 1. 多线程编程基础
print("\n1. 多线程编程基础")
print("- 多线程是指在一个进程内创建多个线程，这些线程共享进程的内存空间")
print("- Python中的多线程由threading模块提供支持")
print("- 多线程适合处理IO密集型任务，可以提高程序的响应速度和吞吐量")
print("- 由于GIL(全局解释器锁)的存在，Python的多线程在CPU密集型任务上可能无法充分利用多核CPU")

# 2. 创建和启动线程
print("\n2. 创建和启动线程")

import threading
import time

# 2.1 使用Thread类创建线程
def thread_function(name):
    """线程要执行的函数"""
    print(f"线程 {name} 开始执行")
    time.sleep(2)  # 模拟线程执行的时间
    print(f"线程 {name} 执行完成")

# 创建并启动多个线程
def create_and_start_threads():
    """创建并启动多个线程"""
    print("\n创建并启动多个线程:")
    
    # 获取当前线程名称
    current_thread = threading.current_thread()
    print(f"当前线程: {current_thread.name}")
    
    # 创建线程对象
    thread1 = threading.Thread(target=thread_function, args=("Thread-1",))
    thread2 = threading.Thread(target=thread_function, args=("Thread-2",))
    thread3 = threading.Thread(target=thread_function, args=("Thread-3",))
    
    # 启动线程
    print("启动所有线程")
    thread1.start()
    thread2.start()
    thread3.start()
    
    # 等待线程完成
    print("等待所有线程完成")
    thread1.join()
    thread2.join()
    thread3.join()
    
    print("所有线程执行完成")

# 执行线程创建示例
create_and_start_threads()

# 2.2 继承Thread类创建线程
class MyThread(threading.Thread):
    """自定义线程类"""
    
    def __init__(self, name):
        """初始化线程"""
        super().__init__(name=name)
        self.name = name
    
    def run(self):
        """线程执行的方法"""
        print(f"自定义线程 {self.name} 开始执行")
        time.sleep(1.5)  # 模拟线程执行的时间
        print(f"自定义线程 {self.name} 执行完成")

# 创建并启动自定义线程
def create_custom_threads():
    """创建并启动自定义线程"""
    print("\n创建并启动自定义线程:")
    
    # 创建自定义线程对象
    custom_thread1 = MyThread("Custom-Thread-1")
    custom_thread2 = MyThread("Custom-Thread-2")
    
    # 启动线程
    print("启动自定义线程")
    custom_thread1.start()
    custom_thread2.start()
    
    # 等待线程完成
    custom_thread1.join()
    custom_thread2.join()
    
    print("所有自定义线程执行完成")

# 执行自定义线程示例
create_custom_threads()

# 3. 线程同步机制
print("\n3. 线程同步机制")
print("- 当多个线程访问共享资源时，需要使用同步机制来避免数据竞争")
print("- Python提供了多种同步原语，如锁、条件变量、信号量等")

# 3.1 使用锁(Lock)进行同步
shared_counter = 0  # 共享资源
counter_lock = threading.Lock()  # 创建锁

def increment_counter(thread_name, iterations):
    """增加计数器的值"""
    global shared_counter
    for i in range(iterations):
        # 获取锁
        with counter_lock:  # 等同于counter_lock.acquire()和counter_lock.release()
            # 临界区 - 同一时间只有一个线程可以执行
            shared_counter += 1
            print(f"线程 {thread_name}: 计数器值 = {shared_counter}")
        # 锁释放后，其他线程可以进入临界区
        time.sleep(0.01)  # 让出一些CPU时间

# 使用锁进行线程同步
def use_locks_for_synchronization():
    """使用锁进行线程同步"""
    print("\n使用锁进行线程同步:")
    global shared_counter
    shared_counter = 0  # 重置计数器
    
    # 创建线程
    thread1 = threading.Thread(target=increment_counter, args=("Lock-Thread-1", 10))
    thread2 = threading.Thread(target=increment_counter, args=("Lock-Thread-2", 10))
    
    # 启动线程
    thread1.start()
    thread2.start()
    
    # 等待线程完成
    thread1.join()
    thread2.join()
    
    print(f"最终计数器值: {shared_counter}")
    print(f"预期计数器值: 20")

# 执行锁同步示例
use_locks_for_synchronization()

# 3.2 使用可重入锁(RLock)
def demonstrate_rlock():
    """演示可重入锁的使用"""
    print("\n使用可重入锁(RLock):")
    
    # 创建可重入锁
    rlock = threading.RLock()
    
    def inner_function():
        """内部函数"""
        with rlock:
            print("进入内部函数，已获取RLock")
            time.sleep(0.5)
            print("离开内部函数，将释放RLock")
    
    def outer_function():
        """外部函数"""
        with rlock:
            print("进入外部函数，已获取RLock")
            # 内部函数可以再次获取同一个锁
            inner_function()
            print("离开外部函数，将释放RLock")
    
    # 创建线程
    thread = threading.Thread(target=outer_function)
    
    # 启动线程
    thread.start()
    thread.join()

# 执行可重入锁示例
demonstrate_rlock()

# 3.3 使用条件变量(Condition)
def demonstrate_condition_variable():
    """演示条件变量的使用"""
    print("\n使用条件变量(Condition):")
    
    # 创建条件变量
    condition = threading.Condition()
    shared_resource = []
    max_items = 5
    
    def producer():
        """生产者线程"""
        for i in range(10):
            time.sleep(0.5)  # 模拟生产过程
            with condition:
                # 检查是否可以生产
                while len(shared_resource) == max_items:
                    print(f"生产者: 缓冲区已满，等待...")
                    condition.wait()  # 等待消费者消费
                
                # 生产一个项目
                item = f"产品-{i}"
                shared_resource.append(item)
                print(f"生产者: 生产了 {item}, 缓冲区: {shared_resource}")
                
                # 通知消费者可以消费了
                condition.notify()
    
    def consumer():
        """消费者线程"""
        for i in range(10):
            time.sleep(1)  # 模拟消费过程
            with condition:
                # 检查是否可以消费
                while not shared_resource:
                    print(f"消费者: 缓冲区为空，等待...")
                    condition.wait()  # 等待生产者生产
                
                # 消费一个项目
                item = shared_resource.pop(0)
                print(f"消费者: 消费了 {item}, 缓冲区: {shared_resource}")
                
                # 通知生产者可以生产了
                condition.notify()
    
    # 创建并启动线程
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
    
    print("生产者-消费者示例完成")

# 执行条件变量示例
demonstrate_condition_variable()

# 3.4 使用信号量(Semaphore)
def demonstrate_semaphore():
    """演示信号量的使用"""
    print("\n使用信号量(Semaphore):")
    
    # 创建信号量，允许最多3个线程同时访问
    semaphore = threading.Semaphore(3)
    
    def access_resource(thread_id):
        """访问共享资源"""
        print(f"线程 {thread_id}: 尝试访问资源")
        with semaphore:  # 获取信号量
            print(f"线程 {thread_id}: 已获取资源访问权限")
            time.sleep(1)  # 模拟使用资源的时间
            print(f"线程 {thread_id}: 释放资源访问权限")
    
    # 创建多个线程
    threads = []
    for i in range(10):
        thread = threading.Thread(target=access_resource, args=(i,))
        threads.append(thread)
    
    # 启动所有线程
    for thread in threads:
        thread.start()
        time.sleep(0.1)  # 稍微间隔启动，便于观察
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()
    
    print("信号量示例完成")

# 执行信号量示例
demonstrate_semaphore()

# 4. 线程池的使用
print("\n4. 线程池的使用")
print("- 线程池可以重用线程，避免频繁创建和销毁线程的开销")
print("- concurrent.futures模块提供了ThreadPoolExecutor类用于创建线程池")

from concurrent.futures import ThreadPoolExecutor

def task_with_result(task_id):
    """一个有返回值的任务"""
    print(f"任务 {task_id} 开始执行")
    time.sleep(1)  # 模拟任务执行时间
    result = task_id * 10
    print(f"任务 {task_id} 执行完成，结果: {result}")
    return result

# 使用线程池
def use_thread_pool():
    """使用线程池"""
    print("\n使用线程池:")
    
    # 创建线程池，最多4个线程
    with ThreadPoolExecutor(max_workers=4) as executor:
        # 提交任务到线程池
        futures = [executor.submit(task_with_result, i) for i in range(10)]
        
        # 获取任务结果
        results = []
        for future in futures:
            result = future.result()  # 阻塞直到任务完成
            results.append(result)
        
        print(f"所有任务完成，结果列表: {results}")
        print(f"结果总和: {sum(results)}")

# 执行线程池示例
use_thread_pool()

# 5. 生产者-消费者模式
print("\n5. 生产者-消费者模式")
print("- 生产者-消费者模式是一种常见的并发设计模式")
print("- 生产者线程生成数据，消费者线程消费数据")
print("- 通常使用队列作为缓冲区")

import queue

# 生产者-消费者模式实现
def producer_consumer_pattern():
    """实现生产者-消费者模式"""
    print("\n生产者-消费者模式实现:")
    
    # 创建线程安全的队列作为缓冲区
    buffer = queue.Queue(maxsize=5)
    
    # 生产完成标志
    exit_flag = False
    
    def producer_task():
        """生产者任务"""
        nonlocal exit_flag
        for i in range(10):
            item = f"产品-{i}"
            try:
                # 尝试放入队列，如果队列已满则阻塞
                buffer.put(item, block=True, timeout=1)
                print(f"生产者: 生产了 {item}, 队列大小: {buffer.qsize()}")
                time.sleep(0.5)  # 模拟生产速度
            except queue.Full:
                print(f"生产者: 队列已满，无法放入 {item}")
        
        # 生产完成
        exit_flag = True
        print("生产者: 生产完成")
    
    def consumer_task():
        """消费者任务"""
        while not exit_flag or not buffer.empty():
            try:
                # 尝试从队列取出，如果队列为空则阻塞
                item = buffer.get(block=True, timeout=1)
                print(f"消费者: 消费了 {item}, 队列大小: {buffer.qsize()}")
                # 标记任务完成
                buffer.task_done()
                time.sleep(1)  # 模拟消费速度
            except queue.Empty:
                # 队列为空时的处理
                if exit_flag:
                    break
                print("消费者: 队列为空，等待...")
        
        print("消费者: 消费完成")
    
    # 创建并启动线程
    producer_thread = threading.Thread(target=producer_task)
    consumer_thread = threading.Thread(target=consumer_task)
    
    producer_thread.start()
    consumer_thread.start()
    
    # 等待线程完成
    producer_thread.join()
    consumer_thread.join()
    
    # 等待队列中所有任务完成
    buffer.join()
    
    print("生产者-消费者模式演示完成")

# 执行生产者-消费者模式示例
producer_consumer_pattern()

# 6. 多线程的实际应用案例
print("\n6. 多线程的实际应用案例")

# 6.1 多线程下载文件
def multithreaded_file_download():
    """多线程下载文件示例"""
    print("\n多线程下载文件示例:")
    
    # 模拟下载任务
    def download_file(file_id):
        """模拟下载单个文件"""
        print(f"开始下载文件 {file_id}")
        time.sleep(1.5)  # 模拟下载时间
        print(f"文件 {file_id} 下载完成")
        return f"file_{file_id}.dat"
    
    # 使用线程池下载多个文件
    with ThreadPoolExecutor(max_workers=3) as executor:
        # 提交10个下载任务
        futures = [executor.submit(download_file, i) for i in range(10)]
        
        # 获取下载结果
        downloaded_files = []
        for i, future in enumerate(futures):
            file_name = future.result()
            downloaded_files.append(file_name)
            print(f"已完成 {i+1}/10 个文件的下载")
        
        print(f"所有文件下载完成: {downloaded_files}")

# 执行多线程下载示例
multithreaded_file_download()

# 6.2 多线程处理数据
def multithreaded_data_processing():
    """多线程数据处理示例"""
    print("\n多线程数据处理示例:")
    
    # 模拟数据处理任务
    def process_data(data_chunk):
        """处理数据块"""
        print(f"开始处理数据块: {data_chunk}")
        time.sleep(0.8)  # 模拟处理时间
        result = sum(data_chunk)
        print(f"数据块 {data_chunk} 处理完成，结果: {result}")
        return result
    
    # 创建数据块
    data_chunks = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    
    # 使用线程池处理数据
    with ThreadPoolExecutor(max_workers=2) as executor:
        # 提交处理任务
        futures = [executor.submit(process_data, chunk) for chunk in data_chunks]
        
        # 获取处理结果
        total_result = 0
        for future in futures:
            total_result += future.result()
        
        print(f"所有数据处理完成，总结果: {total_result}")

# 执行多线程数据处理示例
multithreaded_data_processing()

# 6.3 多线程Web服务器
print("\n6.3 多线程Web服务器")

# 创建一个简单的多线程Web服务器
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """多线程HTTP服务器"""
    daemon_threads = True  # 设置为守护线程，主线程结束时自动结束

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """简单的HTTP请求处理器"""
    
    def do_GET(self):
        """处理GET请求"""
        # 发送响应状态码
        self.send_response(200)
        
        # 发送响应头
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # 模拟处理延迟
        time.sleep(1)
        
        # 发送响应内容
        response_content = f"""
        <html>
        <head><title>多线程Web服务器</title></head>
        <body>
        <h1>Hello, World!</h1>
        <p>当前线程: {threading.current_thread().name}</p>
        <p>请求路径: {self.path}</p>
        <p>时间戳: {time.time()}</p>
        </body>
        </html>
        """
        
        # 写入响应内容
        self.wfile.write(response_content.encode('utf-8'))
        
    def log_message(self, format, *args):
        """覆盖日志方法，避免输出到控制台"""
        pass

# 启动多线程Web服务器
def start_multithreaded_web_server():
    """启动多线程Web服务器"""
    print("\n启动多线程Web服务器:")
    
    server_address = ('localhost', 8000)
    httpd = ThreadedHTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print(f"多线程Web服务器已启动，访问地址: http://{server_address[0]}:{server_address[1]}")
    print("按Ctrl+C停止服务器")
    
    try:
        # 注意：为了不阻塞主线程，这里不实际启动服务器
        # httpd.serve_forever()
        print("(演示模式，未实际启动服务器)")
    except Exception as e:
        print(f"服务器发生错误: {e}")
    finally:
        # 关闭服务器
        httpd.server_close()
        print("多线程Web服务器已关闭")

# 执行多线程Web服务器示例
start_multithreaded_web_server()

# 7. 多线程编程的最佳实践
print("\n7. 多线程编程的最佳实践")
print("- 避免使用共享状态，尽可能使用不可变对象")
print("- 如果必须使用共享状态，使用适当的同步机制(如锁、队列等)")
print("- 优先使用线程池而不是手动创建和管理线程")
print("- 注意Python的GIL限制，对于CPU密集型任务考虑使用多进程")
print("- 使用守护线程或适当的机制确保主线程能够优雅地退出")
print("- 避免在多线程环境中使用阻塞的IO操作，特别是长时间阻塞")
print("- 处理线程异常，避免异常导致线程意外终止且不通知主线程")
print("- 使用threading.local()创建线程本地存储，避免线程间的数据竞争")
print("- 对于复杂的同步需求，考虑使用高级同步原语(如Queue)而不是低级原语(如Lock)")
print("- 设计线程安全的类和函数，明确其线程安全性保证")

# 8. 线程本地存储
print("\n8. 线程本地存储")

# 线程本地存储用于存储线程特有的数据
def demonstrate_thread_local_storage():
    """演示线程本地存储的使用"""
    print("\n使用线程本地存储:")
    
    # 创建线程本地存储对象
    thread_local = threading.local()
    
    def worker():
        """工作线程函数"""
        # 为每个线程设置特有的值
        thread_local.value = threading.current_thread().name
        print(f"线程 {threading.current_thread().name}: 初始值 = {thread_local.value}")
        
        # 修改线程本地值
        thread_local.value = f"{thread_local.value}-modified"
        print(f"线程 {threading.current_thread().name}: 修改后的值 = {thread_local.value}")
        
        # 模拟线程执行时间
        time.sleep(0.5)
        
        # 再次访问线程本地值
        print(f"线程 {threading.current_thread().name}: 最终值 = {thread_local.value}")
    
    # 创建多个线程
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, name=f"Thread-{i}")
        threads.append(thread)
    
    # 启动所有线程
    for thread in threads:
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()
    
    print("线程本地存储示例完成")

# 执行线程本地存储示例
demonstrate_thread_local_storage()

# 9. 多线程的优缺点
print("\n9. 多线程的优缺点")
print("\n优点:")
print("- 提高程序的响应速度，特别是对于IO密集型任务")
print("- 充分利用CPU资源，特别是在多核系统上")
print("- 线程间通信方便，共享内存空间")
print("- 相比多进程，线程创建和切换的开销较小")
print("\n缺点:")
print("- Python由于GIL的存在，多线程在CPU密集型任务上无法充分利用多核")
print("- 多线程编程容易引入难以调试的问题，如死锁、竞态条件等")
print("- 线程同步会带来额外的开销")
print("- 共享状态的管理比较复杂")

print("\n总结：")
print("多线程编程是处理并发任务的重要方式，可以显著提高程序的性能和响应性")
print("Python的threading模块提供了丰富的功能来支持多线程编程")
print("在实际项目中，应根据任务特性选择合适的并发模型")
print("对于IO密集型任务，多线程是一个很好的选择")
print("对于CPU密集型任务，可能需要考虑使用多进程或者其他语言")
print("同时，一定要注意线程安全问题，正确使用同步机制，避免常见的并发陷阱")