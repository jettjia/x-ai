# -*- coding: utf-8 -*-

"""网络编程实际应用案例

这个模块包含了网络编程的实际应用案例，如端口扫描器、文件下载工具和代理服务器等。
"""

import socket
import urllib.request
import urllib.error
import http.server
import socketserver
import os


class PortScanner:
    """简单的端口扫描器"""
    
    def __init__(self):
        """初始化端口扫描器"""
        pass
    
    def scan(self, host, start_port, end_port, timeout=0.1):
        """扫描指定主机的端口范围
        
        Args:
            host (str): 要扫描的主机名或IP地址
            start_port (int): 起始端口号
            end_port (int): 结束端口号
            timeout (float): 连接超时时间，默认为0.1秒
            
        Returns:
            list: 开放的端口列表
        """
        print(f"开始扫描主机 {host} 的端口 {start_port}-{end_port}")
        
        open_ports = []
        
        try:
            # 获取主机的IP地址
            ip = socket.gethostbyname(host)
            print(f"主机 {host} 的IP地址是 {ip}")
            
            # 扫描端口范围
            for port in range(start_port, end_port + 1):
                # 创建socket对象
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)  # 设置超时时间
                
                # 尝试连接端口
                result = sock.connect_ex((ip, port))
                
                # 如果端口开放（返回值为0）
                if result == 0:
                    try:
                        # 尝试获取端口服务名称
                        service = socket.getservbyport(port)
                        print(f"端口 {port}: 开放 ({service})")
                    except:
                        print(f"端口 {port}: 开放")
                    open_ports.append(port)
                
                # 关闭socket
                sock.close()
            
            print(f"扫描完成。发现 {len(open_ports)} 个开放端口: {open_ports}")
            
        except socket.gaierror:
            print(f"无法解析主机名 {host}")
        except socket.error:
            print(f"无法连接到主机 {host}")
        except Exception as e:
            print(f"扫描过程中发生错误: {e}")
        
        return open_ports


class FileDownloader:
    """文件下载工具"""
    
    def __init__(self):
        """初始化文件下载工具"""
        pass
    
    def download(self, url, save_path):
        """从指定URL下载文件
        
        Args:
            url (str): 文件的URL地址
            save_path (str): 保存文件的路径
            
        Returns:
            bool: 下载是否成功
        """
        try:
            print(f"开始下载文件: {url}")
            
            # 确保保存目录存在
            save_dir = os.path.dirname(save_path)
            if save_dir and not os.path.exists(save_dir):
                os.makedirs(save_dir)
                print(f"创建保存目录: {save_dir}")
            
            print(f"保存路径: {save_path}")
            
            # 使用urllib下载文件
            urllib.request.urlretrieve(url, save_path)
            print(f"文件下载完成: {save_path}")
            
            return True
            
        except urllib.error.URLError as e:
            print(f"URL错误: {e}")
        except IOError as e:
            print(f"IO错误: {e}")
        except Exception as e:
            print(f"下载过程中发生错误: {e}")
        
        return False


class ProxyHandler(http.server.BaseHTTPRequestHandler):
    """简单的HTTP代理处理器"""
    
    def do_GET(self):
        """处理GET请求"""
        try:
            # 打印请求信息
            print(f"代理请求: {self.path}")
            
            # 创建请求对象
            req = urllib.request.Request(self.path, headers=self.headers)
            
            # 发送请求到目标服务器
            with urllib.request.urlopen(req) as response:
                # 获取响应状态码和头信息
                self.send_response(response.status)
                
                # 复制响应头
                for header, value in response.getheaders():
                    if header.lower() != 'transfer-encoding':
                        self.send_header(header, value)
                self.end_headers()
                
                # 复制响应内容
                self.wfile.write(response.read())
                
        except Exception as e:
            self.send_error(500, f"代理错误: {str(e)}")
    
    # 可以根据需要实现其他HTTP方法的处理，如POST、PUT等
    do_POST = do_GET
    do_PUT = do_GET
    do_DELETE = do_GET


class SimpleProxyServer:
    """简单的HTTP代理服务器"""
    
    def __init__(self, host='localhost', port=8889):
        """初始化代理服务器
        
        Args:
            host (str): 服务器主机地址，默认为'localhost'
            port (int): 服务器端口号，默认为8889
        """
        self.host = host
        self.port = port
        self.httpd = None
    
    def start(self, block=True):
        """启动代理服务器
        
        Args:
            block (bool): 是否阻塞主线程，默认为True
        """
        try:
            # 创建多线程TCP服务器
            self.httpd = socketserver.ThreadingTCPServer((self.host, self.port), ProxyHandler)
            
            print(f"简单代理服务器已启动，监听端口: {self.port}")
            print("按Ctrl+C停止服务器")
            
            if block:
                # 阻塞模式，一直运行直到被中断
                self.httpd.serve_forever()
            else:
                # 非阻塞模式，仅打印信息不实际启动（避免阻塞主线程）
                print("(演示模式，未实际启动服务器)")
                
        except Exception as e:
            print(f"代理服务器发生错误: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """停止代理服务器"""
        if self.httpd:
            self.httpd.server_close()
            print("代理服务器已关闭")


def demo_applications():
    """演示网络编程应用案例"""
    print("\n演示网络编程实际应用案例:")
    
    # 1. 演示端口扫描器
    print("\n1. 简单的端口扫描器:")
    scanner = PortScanner()
    # 只扫描少量端口以避免超时
    scanner.scan("localhost", 80, 100)
    
    # 2. 演示文件下载工具
    print("\n2. 文件下载工具:")
    downloader = FileDownloader()
    # 尝试下载一个小文件（演示用）
    demo_file_url = "https://httpbin.org/image/jpeg"
    demo_save_path = "sample_files/demo_image.jpg"
    downloader.download(demo_file_url, demo_save_path)
    
    # 3. 演示代理服务器
    print("\n3. 简单的代理服务器:")
    proxy_server = SimpleProxyServer()
    proxy_server.start(block=False)  # 非阻塞模式


if __name__ == "__main__":
    # 当直接运行此模块时，演示网络编程应用案例
    demo_applications()