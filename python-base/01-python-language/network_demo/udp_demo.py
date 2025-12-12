# -*- coding: utf-8 -*-

"""UDP协议编程示例

这个模块演示了如何使用Python的socket库实现UDP协议的客户端和服务器通信。
"""

import socket
import threading
import time


class UDPServer:
    """UDP服务器类"""
    
    def __init__(self, host='localhost', port=9999):
        """初始化UDP服务器
        
        Args:
            host (str): 服务器主机地址，默认为'localhost'
            port (int): 服务器端口号，默认为9999
        """
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        
    def start(self):
        """启动UDP服务器"""
        try:
            # 创建socket对象
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # 设置端口可重用
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # 绑定IP地址和端口
            self.server_socket.bind((self.host, self.port))
            self.running = True
            print(f"UDP服务器已启动，监听地址: {self.host}:{self.port}")
            print("等待客户端消息...")
            
            # 接收客户端消息
            while self.running:
                # 接收客户端发送的数据和地址
                data, client_address = self.server_socket.recvfrom(1024)
                message = data.decode('utf-8')
                print(f"收到来自客户端 {client_address} 的消息: {message}")
                
                # 向客户端发送响应
                response = "Hello, I am UDP Server!"
                self.server_socket.sendto(response.encode('utf-8'), client_address)
                print(f"已向客户端 {client_address} 发送响应: {response}")
                
                # 只处理一个请求后退出（演示用）
                break
                
        except Exception as e:
            print(f"UDP服务器发生错误: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """停止UDP服务器"""
        if self.server_socket:
            self.running = False
            self.server_socket.close()
            print("UDP服务器已关闭")


class UDPClient:
    """UDP客户端类"""
    
    def __init__(self, host='localhost', port=9999):
        """初始化UDP客户端
        
        Args:
            host (str): 服务器主机地址，默认为'localhost'
            port (int): 服务器端口号，默认为9999
        """
        self.host = host
        self.port = port
        self.client_socket = None
    
    def send_message(self):
        """向UDP服务器发送消息并等待响应"""
        try:
            # 创建socket对象
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # 服务器地址
            server_address = (self.host, self.port)
            
            # 向服务器发送数据
            message = "Hello, I am UDP Client!"
            self.client_socket.sendto(message.encode('utf-8'), server_address)
            print(f"已向服务器 {server_address} 发送消息: {message}")
            
            # 接收服务器响应
            data, server_address = self.client_socket.recvfrom(1024)
            response = data.decode('utf-8')
            print(f"收到来自服务器 {server_address} 的响应: {response}")
            
        except Exception as e:
            print(f"UDP客户端发生错误: {e}")
        finally:
            # 关闭socket
            if self.client_socket:
                self.client_socket.close()
                print("UDP客户端已关闭")


def demo_udp_communication():
    """演示UDP服务器和客户端通信"""
    print("\n演示UDP服务器和客户端通信:")
    print("1. 首先启动UDP服务器")
    print("2. 然后启动UDP客户端发送消息")
    
    # 创建服务器实例
    server = UDPServer()
    
    # 在单独的线程中启动UDP服务器
    server_thread = threading.Thread(target=server.start)
    server_thread.daemon = True
    server_thread.start()
    
    # 等待服务器启动
    time.sleep(1)
    
    # 创建并启动客户端
    client = UDPClient()
    client.send_message()
    
    # 等待服务器线程结束
    time.sleep(1)
    
    # 停止服务器
    server.stop()


if __name__ == "__main__":
    # 当直接运行此模块时，演示UDP通信
    demo_udp_communication()