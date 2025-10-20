# -*- coding: utf-8 -*-

"""HTTP服务器编程示例

这个模块演示了如何使用Python的http.server模块创建HTTP服务器。
"""

import http.server
import socketserver


class SimpleHTTPServer:
    """简单的HTTP服务器类"""
    
    def __init__(self, host='localhost', port=8000):
        """初始化简单HTTP服务器
        
        Args:
            host (str): 服务器主机地址，默认为'localhost'
            port (int): 服务器端口号，默认为8000
        """
        self.host = host
        self.port = port
        self.httpd = None
    
    def start(self, block=True):
        """启动简单HTTP服务器
        
        Args:
            block (bool): 是否阻塞主线程，默认为True
        """
        try:
            # 创建TCP服务器
            Handler = http.server.SimpleHTTPRequestHandler
            self.httpd = socketserver.TCPServer((self.host, self.port), Handler)
            
            print(f"简单HTTP服务器已启动，访问地址: http://{self.host}:{self.port}")
            print("按Ctrl+C停止服务器")
            
            if block:
                # 阻塞模式，一直运行直到被中断
                self.httpd.serve_forever()
            else:
                # 非阻塞模式，仅打印信息不实际启动（避免阻塞主线程）
                print("(演示模式，未实际启动服务器)")
                
        except Exception as e:
            print(f"HTTP服务器发生错误: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """停止HTTP服务器"""
        if self.httpd:
            self.httpd.server_close()
            print("HTTP服务器已关闭")


class CustomHTTPHandler(http.server.BaseHTTPRequestHandler):
    """自定义HTTP请求处理器"""
    
    def do_GET(self):
        """处理GET请求"""
        # 发送响应状态码
        self.send_response(200)
        
        # 发送响应头
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # 发送响应内容
        response_content = """
        <html>
        <head><title>Custom HTTP Server</title></head>
        <body>
        <h1>Hello, World!</h1>
        <p>This is a custom HTTP server.</p>
        <p>Request path: {}</p>
        </body>
        </html>
        """
        
        # 写入响应内容
        self.wfile.write(response_content.format(self.path).encode('utf-8'))
    
    def do_POST(self):
        """处理POST请求"""
        # 获取请求数据长度
        content_length = int(self.headers['Content-Length'])
        
        # 读取请求数据
        post_data = self.rfile.read(content_length)
        
        # 发送响应状态码
        self.send_response(200)
        
        # 发送响应头
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # 发送响应内容
        response_content = f"""
        {
            "status": "success",
            "received_data": "{data_str}",
            "method": "POST",
            "path": "{self.path}"
        }
        """
        
        # 写入响应内容
        self.wfile.write(response_content.format(post_data.decode('utf-8'), self.path).encode('utf-8'))


class CustomHTTPServer:
    """自定义HTTP服务器类"""
    
    def __init__(self, host='localhost', port=8001):
        """初始化自定义HTTP服务器
        
        Args:
            host (str): 服务器主机地址，默认为'localhost'
            port (int): 服务器端口号，默认为8001
        """
        self.host = host
        self.port = port
        self.httpd = None
    
    def start(self, block=True):
        """启动自定义HTTP服务器
        
        Args:
            block (bool): 是否阻塞主线程，默认为True
        """
        try:
            # 创建TCP服务器
            self.httpd = socketserver.TCPServer((self.host, self.port), CustomHTTPHandler)
            
            print(f"自定义HTTP服务器已启动，访问地址: http://{self.host}:{self.port}")
            print("按Ctrl+C停止服务器")
            
            if block:
                # 阻塞模式，一直运行直到被中断
                self.httpd.serve_forever()
            else:
                # 非阻塞模式，仅打印信息不实际启动（避免阻塞主线程）
                print("(演示模式，未实际启动服务器)")
                
        except Exception as e:
            print(f"自定义HTTP服务器发生错误: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """停止HTTP服务器"""
        if self.httpd:
            self.httpd.server_close()
            print("自定义HTTP服务器已关闭")


def demo_http_servers():
    """演示HTTP服务器功能"""
    print("\n演示HTTP服务器功能:")
    
    # 启动简单的HTTP服务器（非阻塞模式）
    print("\n1. 简单的HTTP服务器:")
    simple_server = SimpleHTTPServer()
    simple_server.start(block=False)  # 非阻塞模式
    
    # 启动自定义的HTTP服务器（非阻塞模式）
    print("\n2. 自定义HTTP服务器:")
    custom_server = CustomHTTPServer()
    custom_server.start(block=False)  # 非阻塞模式


if __name__ == "__main__":
    # 当直接运行此模块时，演示HTTP服务器功能
    demo_http_servers()