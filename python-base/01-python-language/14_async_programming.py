#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python异步编程示例

print("Python 异步编程示例\n" + "="*50)

# 1. 异步编程基础
print("\n1. 异步编程基础")
print("- 异步编程是一种编程范式，允许程序在等待某些操作（如IO）完成时继续执行其他任务")
print("- Python从3.5版本开始引入了async/await语法，使异步编程更加简洁明了")
print("- 核心概念：协程(coroutine)、事件循环(event loop)、任务(task)、异步IO")
print("- 主要模块：asyncio（Python标准库）")

# 2. 协程的基本使用
print("\n2. 协程的基本使用")

import asyncio

# 定义一个简单的协程函数
async def simple_coroutine():
    """一个简单的协程函数"""
    print("协程开始执行")
    # 使用await暂停协程执行
    await asyncio.sleep(1)
    print("协程执行完成")
    return "协程返回值"

# 运行协程函数
def run_simple_coroutine():
    """运行简单的协程函数"""
    print("\n运行简单的协程函数:")
    # 获取事件循环
    loop = asyncio.get_event_loop()
    
    try:
        # 运行协程直到完成
        result = loop.run_until_complete(simple_coroutine())
        print(f"协程执行结果: {result}")
    finally:
        # 关闭事件循环
        loop.close()

# 在Python 3.7+中，可以使用更简单的方式运行协程
def run_coroutine_with_run():
    """使用asyncio.run()运行协程"""
    print("\n使用asyncio.run()运行协程:")
    try:
        # Python 3.7+ 提供的简化接口
        result = asyncio.run(simple_coroutine())
        print(f"协程执行结果: {result}")
    except RuntimeError as e:
        # 如果当前环境不支持多次调用asyncio.run()，则跳过
        print(f"注意: {e}")

# 执行协程示例
run_simple_coroutine()
run_coroutine_with_run()

# 3. 协程的高级使用
print("\n3. 协程的高级使用")

# 3.1 等待多个协程完成
async def task1():
    """任务1"""
    print("任务1开始")
    await asyncio.sleep(2)
    print("任务1完成")
    return "任务1结果"

async def task2():
    """任务2"""
    print("任务2开始")
    await asyncio.sleep(1)
    print("任务2完成")
    return "任务2结果"

async def task3():
    """任务3"""
    print("任务3开始")
    await asyncio.sleep(3)
    print("任务3完成")
    return "任务3结果"

async def main_tasks():
    """同时运行多个协程"""
    print("\n等待多个协程完成:")
    
    # 方式1: 按顺序等待
    print("\n方式1: 按顺序等待协程")
    result1 = await task1()
    result2 = await task2()
    result3 = await task3()
    print(f"按顺序执行结果: {result1}, {result2}, {result3}")
    
    # 方式2: 并发执行并等待所有协程完成
    print("\n方式2: 并发执行协程")
    results = await asyncio.gather(
        task1(),
        task2(),
        task3()
    )
    print(f"并发执行结果: {results}")

# 运行多任务示例
def run_multiple_tasks():
    """运行多个协程任务"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main_tasks())
    finally:
        loop.close()

# 执行多任务示例
run_multiple_tasks()

# 3.2 创建和管理任务
async def create_and_manage_tasks():
    """创建和管理任务"""
    print("\n创建和管理任务:")
    
    # 创建任务
    task = asyncio.create_task(task1())
    print(f"任务状态: {task}")
    
    # 等待任务完成
    result = await task
    print(f"任务结果: {result}")
    print(f"任务完成后的状态: {task}")
    
    # 创建多个任务
    tasks = [
        asyncio.create_task(task1()),
        asyncio.create_task(task2()),
        asyncio.create_task(task3())
    ]
    
    # 等待所有任务完成
    done, pending = await asyncio.wait(tasks, timeout=None)
    
    print(f"完成的任务数量: {len(done)}")
    print(f"待处理的任务数量: {len(pending)}")
    
    # 获取任务结果
    for task in done:
        try:
            result = task.result()
            print(f"任务结果: {result}")
        except Exception as e:
            print(f"任务异常: {e}")

# 运行任务管理示例
def run_task_management():
    """运行任务管理示例"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(create_and_manage_tasks())
    finally:
        loop.close()

# 执行任务管理示例
run_task_management()

# 4. 异步IO操作
print("\n4. 异步IO操作")

# 4.1 异步文件IO
async def async_file_operations():
    """异步文件IO操作"""
    print("\n异步文件IO操作:")
    
    # 注意：Python的标准文件IO操作是阻塞的
    # 这里使用asyncio的to_thread()函数在单独的线程中执行阻塞操作
    
    # 写入文件
    async def write_file():
        print("开始写入文件")
        # 使用to_thread运行阻塞的文件写入操作
        await asyncio.to_thread(lambda: \
            open('sample_files/async_file.txt', 'w', encoding='utf-8').write(
                "这是异步写入的第一行\n这是异步写入的第二行\n"
            )
        )
        print("文件写入完成")
    
    # 读取文件
    async def read_file():
        print("开始读取文件")
        content = await asyncio.to_thread(lambda: \
            open('sample_files/async_file.txt', 'r', encoding='utf-8').read()
        )
        print(f"文件内容: {content}")
        return content
    
    # 并发执行读写操作
    await asyncio.gather(write_file(), read_file())

# 运行异步文件IO示例
def run_async_file_operations():
    """运行异步文件IO示例"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(async_file_operations())
    finally:
        loop.close()

# 执行异步文件IO示例
run_async_file_operations()

# 4.2 异步网络请求
async def async_network_requests():
    """异步网络请求"""
    print("\n异步网络请求:")
    
    # 注意：requests库是阻塞的，这里我们模拟异步网络请求
    # 在实际项目中，可以使用aiohttp等异步HTTP客户端库
    
    async def fetch_url(url, delay):
        """模拟异步获取URL内容"""
        print(f"开始请求: {url}")
        await asyncio.sleep(delay)  # 模拟网络延迟
        print(f"请求完成: {url}")
        return f"{url} 的响应内容"
    
    # 并发请求多个URL
    results = await asyncio.gather(
        fetch_url("https://www.example.com", 1),
        fetch_url("https://www.example.org", 2),
        fetch_url("https://www.example.net", 1.5)
    )
    
    print(f"所有请求完成，结果: {results}")

# 运行异步网络请求示例
def run_async_network_requests():
    """运行异步网络请求示例"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(async_network_requests())
    finally:
        loop.close()

# 执行异步网络请求示例
run_async_network_requests()

# 5. 异步上下文管理器
print("\n5. 异步上下文管理器")

# 定义异步上下文管理器
class AsyncContextManager:
    """一个简单的异步上下文管理器"""
    
    async def __aenter__(self):
        """进入上下文管理器"""
        print("进入异步上下文管理器")
        await asyncio.sleep(0.5)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器"""
        print("退出异步上下文管理器")
        await asyncio.sleep(0.5)
        # 返回False表示不抑制异常
        return False

async def use_async_context_manager():
    """使用异步上下文管理器"""
    print("\n使用异步上下文管理器:")
    
    # 使用async with语法
    async with AsyncContextManager() as manager:
        print("在异步上下文管理器中执行操作")
        await asyncio.sleep(1)

# 运行异步上下文管理器示例
def run_async_context_manager():
    """运行异步上下文管理器示例"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(use_async_context_manager())
    finally:
        loop.close()

# 执行异步上下文管理器示例
run_async_context_manager()

# 6. 异步队列
print("\n6. 异步队列")

# 异步队列用于在协程之间安全地传递数据
async def producer(queue, n):
    """生产者：向队列中添加数据"""
    for i in range(n):
        # 模拟生产过程
        await asyncio.sleep(0.5)
        item = f"产品 {i}"
        await queue.put(item)
        print(f"生产者添加: {item}, 队列大小: {queue.qsize()}")
    
    # 发送完成信号
    await queue.put(None)
    print("生产者完成")

async def consumer(queue):
    """消费者：从队列中获取数据"""
    while True:
        # 获取队列中的数据
        item = await queue.get()
        
        # 检查是否是完成信号
        if item is None:
            # 通知队列任务完成
            queue.task_done()
            break
        
        # 模拟消费过程
        await asyncio.sleep(1)
        print(f"消费者处理: {item}")
        
        # 通知队列任务完成
        queue.task_done()
    
    print("消费者完成")

async def use_async_queue():
    """使用异步队列"""
    print("\n使用异步队列:")
    
    # 创建异步队列，最大容量为5
    queue = asyncio.Queue(maxsize=5)
    
    # 创建生产者和消费者任务
    producer_task = asyncio.create_task(producer(queue, 5))
    consumer_task = asyncio.create_task(consumer(queue))
    
    # 等待生产者完成
    await producer_task
    
    # 等待队列中的所有任务完成
    await queue.join()
    
    # 取消消费者任务（如果它还在运行）
    consumer_task.cancel()
    
    try:
        # 等待消费者任务结束
        await consumer_task
    except asyncio.CancelledError:
        print("消费者任务被取消")

# 运行异步队列示例
def run_async_queue():
    """运行异步队列示例"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(use_async_queue())
    finally:
        loop.close()

# 执行异步队列示例
run_async_queue()

# 7. 异步网络服务器
print("\n7. 异步网络服务器")

# 创建一个简单的异步TCP服务器
async def handle_client(reader, writer):
    """处理客户端连接"""
    # 获取客户端地址
    addr = writer.get_extra_info('peername')
    print(f"客户端连接: {addr}")
    
    try:
        # 接收数据
        data = await reader.read(100)
        message = data.decode()
        print(f"收到消息: {message} 来自 {addr}")
        
        # 发送响应
        response = f"服务器收到: {message}"
        writer.write(response.encode())
        await writer.drain()
        print(f"已发送响应: {response} 到 {addr}")
    except Exception as e:
        print(f"处理客户端 {addr} 时发生错误: {e}")
    finally:
        # 关闭连接
        print(f"客户端断开连接: {addr}")
        writer.close()
        await writer.wait_closed()

async def start_async_tcp_server():
    """启动异步TCP服务器"""
    print("\n启动异步TCP服务器:")
    
    # 创建服务器
    server = await asyncio.start_server(
        handle_client, 'localhost', 8888
    )
    
    # 获取服务器地址
    addr = server.sockets[0].getsockname()
    print(f"异步TCP服务器启动在 {addr}")
    
    try:
        # 注意：为了不阻塞主线程，这里不实际启动服务器
        # async with server:
        #     await server.serve_forever()
        print("(演示模式，未实际启动服务器)")
    except Exception as e:
        print(f"服务器发生错误: {e}")
    finally:
        # 关闭服务器
        server.close()
        print("异步TCP服务器已关闭")

# 运行异步TCP服务器示例
def run_async_tcp_server():
    """运行异步TCP服务器示例"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(start_async_tcp_server())
    finally:
        loop.close()

# 执行异步TCP服务器示例
run_async_tcp_server()

# 8. 异步编程实际应用案例
print("\n8. 异步编程实际应用案例")

# 8.1 异步Web爬虫
async def async_web_crawler():
    """异步Web爬虫示例"""
    print("\n异步Web爬虫示例:")
    
    # 模拟爬取多个URL
    async def crawl_url(url, delay):
        """模拟爬取单个URL"""
        print(f"开始爬取: {url}")
        await asyncio.sleep(delay)  # 模拟网络请求延迟
        print(f"完成爬取: {url}")
        return f"{url} 的爬取结果"
    
    # 要爬取的URL列表
    urls = [
        ("https://www.example.com/page1", 1),
        ("https://www.example.com/page2", 0.5),
        ("https://www.example.com/page3", 2),
        ("https://www.example.com/page4", 0.8),
        ("https://www.example.com/page5", 1.5),
    ]
    
    # 创建爬取任务
    tasks = [crawl_url(url, delay) for url, delay in urls]
    
    # 并发执行所有爬取任务
    results = await asyncio.gather(*tasks)
    
    print(f"所有URL爬取完成，共 {len(results)} 个结果")

# 运行异步Web爬虫示例
def run_async_web_crawler():
    """运行异步Web爬虫示例"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(async_web_crawler())
    finally:
        loop.close()

# 执行异步Web爬虫示例
run_async_web_crawler()

# 8.2 异步API服务器
async def async_api_server():
    """异步API服务器示例"""
    print("\n异步API服务器示例:")
    
    # 模拟API端点
    async def api_endpoint(path, delay):
        """模拟API端点处理"""
        print(f"处理API请求: {path}")
        await asyncio.sleep(delay)  # 模拟处理延迟
        print(f"完成API请求: {path}")
        return {
            "path": path,
            "status": "success",
            "data": f"{path} 的响应数据"
        }
    
    # 模拟API请求
    async def make_api_requests():
        """模拟多个API请求"""
        # 创建API请求任务
        tasks = [
            api_endpoint("/api/users", 1),
            api_endpoint("/api/products", 0.7),
            api_endpoint("/api/orders", 1.2),
        ]
        
        # 并发执行所有API请求
        results = await asyncio.gather(*tasks)
        
        for result in results:
            print(f"API响应: {result}")
    
    # 运行API请求
    await make_api_requests()

# 运行异步API服务器示例
def run_async_api_server():
    """运行异步API服务器示例"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(async_api_server())
    finally:
        loop.close()

# 执行异步API服务器示例
run_async_api_server()

# 9. 异步编程的最佳实践
print("\n9. 异步编程的最佳实践")
print("- 优先使用async/await语法，避免使用旧式的回调函数")
print("- 对于IO密集型任务使用异步编程，CPU密集型任务仍然适合使用多线程或多进程")
print("- 避免在异步代码中使用阻塞的IO操作，这会阻塞整个事件循环")
print("- 使用asyncio的内置函数（如gather、wait等）来管理多个协程")
print("- 使用异步上下文管理器（async with）来管理资源")
print("- 对于需要长时间运行的CPU密集型操作，考虑使用asyncio.to_thread()或loop.run_in_executor()")
print("- 合理设置超时时间，避免协程无限等待")
print("- 处理协程中的异常，使用try/except块捕获可能的异常")
print("- 对于网络请求，使用专门的异步库（如aiohttp）而不是阻塞的库（如requests）")
print("- 理解异步编程的复杂性，不要为了异步而异步，简单的场景使用同步代码可能更清晰")

# 10. 常见异步库介绍
print("\n10. 常见异步库介绍")
print("- asyncio: Python标准库中的异步IO框架")
print("- aiohttp: 异步HTTP客户端/服务器库")
print("- aiomysql/aiopg: 异步数据库驱动")
print("- aiofiles: 异步文件操作库")
print("- motor: 异步MongoDB驱动")
print("- fastapi: 基于Python类型提示的高性能异步Web框架")
print("- starlette: 轻量级异步ASGI框架")
print("- trio: 另一个异步IO库，专注于易用性和正确性")

print("\n总结：")
print("异步编程是处理IO密集型任务的有效方式，可以显著提高程序的并发性能")
print("Python的async/await语法使异步编程变得更加简单和直观")
print("asyncio模块提供了丰富的功能来支持异步编程，包括协程、任务、事件循环等")
print("在实际项目中，应根据任务特性选择合适的编程范式，IO密集型任务优先考虑异步编程")
print("同时也要注意异步编程的复杂性，避免滥用异步导致代码难以理解和维护")