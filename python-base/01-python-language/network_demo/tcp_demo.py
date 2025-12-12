# -*- coding: utf-8 -*-

"""TCP协议编程示例

这个模块演示了如何使用Python的socket库实现TCP协议的客户端和服务器通信。
"""

import socket
import threading
import time


class TCPServer:
    """TCP服务器类"""
    
    def __init__(self, host='localhost', port=8888):
        """初始化TCP服务器
        
        Args:
            host (str): 服务器主机地址，默认为'localhost'
            port (int): 服务器端口号，默认为8888
        """
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        
    def start(self):
        """启动TCP服务器"""
        try:
            # 创建socket对象
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # 设置端口可重用
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # 绑定IP地址和端口
            self.server_socket.bind((self.host, self.port))
            
            # 开始监听连接
            self.server_socket.listen(5)
            self.running = True
            print(f"TCP服务器已启动，监听地址: {self.host}:{self.port}")
            
            # 接受客户端连接
            while self.running:
                client_socket, client_address = self.server_socket.accept()
                print(f"客户端已连接: {client_address}")
                
                # 处理客户端请求
                self._handle_client(client_socket, client_address)
                
        except Exception as e:
            print(f"TCP服务器发生错误: {e}")
        finally:
            self.stop()
    
    def _handle_client(self, client_socket, client_address):
        """处理客户端连接
        
        Args:
            client_socket (socket.socket): 客户端socket对象
            client_address (tuple): 客户端地址
        """
        try:
            # 接收客户端发送的数据
            data = client_socket.recv(1024).decode('utf-8')
            print(f"收到客户端消息: {data}")
            
            # 向客户端发送响应
            response = "Hello, I am TCP Server!"
            client_socket.send(response.encode('utf-8'))
            print(f"已向客户端发送响应: {response}")
            
        except Exception as e:
            print(f"处理客户端连接时发生错误: {e}")
        finally:
            # 关闭客户端连接
            client_socket.close()
    
    def stop(self):
        """停止TCP服务器"""
        if self.server_socket:
            self.running = False
            self.server_socket.close()
            print("TCP服务器已关闭")


class TCPClient:
    """TCP客户端类"""
    
    def __init__(self, host='localhost', port=8888):
        """初始化TCP客户端
        
        Args:
            host (str): 服务器主机地址，默认为'localhost'
            port (int): 服务器端口号，默认为8888
        """
        self.host = host
        self.port = port
        self.client_socket = None
    
    def connect(self):
        """连接到TCP服务器并进行通信"""
        try:
            # 创建socket对象
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # 连接服务器
            self.client_socket.connect((self.host, self.port))
            print(f"已连接到服务器: {self.host}:{self.port}")
            
            # 向服务器发送数据
            message = "Hello, I am TCP Client!"
            self.client_socket.send(message.encode('utf-8'))
            print(f"已向服务器发送消息: {message}")
            
            # 接收服务器响应
            data = self.client_socket.recv(1024).decode('utf-8')
            print(f"收到服务器响应: {data}")
            
        except Exception as e:
            print(f"TCP客户端发生错误: {e}")
        finally:
            # 关闭连接
            if self.client_socket:
                self.client_socket.close()
                print("TCP客户端已关闭")


def demo_tcp_communication():
    """演示TCP服务器和客户端通信"""
    print("\n演示TCP服务器和客户端通信:")
    print("1. 首先启动TCP服务器")
    print("2. 然后启动TCP客户端连接服务器")
    
    # 创建服务器实例
    server = TCPServer()
    
    # 在单独的线程中启动TCP服务器
    server_thread = threading.Thread(target=server.start)
    server_thread.daemon = True  # 设为守护线程，主线程结束时自动结束
    server_thread.start()
    
    # 等待服务器启动
    time.sleep(1)
    
    # 创建并启动客户端
    client = TCPClient()
    client.connect()
    
    # 等待服务器线程结束
    time.sleep(1)
    
    # 停止服务器
    server.stop()


if __name__ == "__main__":
    # 当直接运行此模块时，演示TCP通信
    demo_tcp_communication()