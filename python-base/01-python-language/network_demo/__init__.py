# -*- coding: utf-8 -*-

"""网络编程演示包

这个包包含了Python网络编程的各种示例代码，包括：
- TCP协议通信
- UDP协议通信
- HTTP客户端编程
- HTTP服务器实现
- WebSocket编程
- 网络应用案例
"""

__version__ = "1.0"
greeting = "欢迎使用Python网络编程演示包！"

# 定义包的公共API
__all__ = ['tcp_demo', 'udp_demo', 'http_client', 'http_server', 'websocket_demo', 'applications']

# 导入各个模块
try:
    import network_demo.tcp_demo
    import network_demo.udp_demo
    import network_demo.http_client
    import network_demo.http_server
    import network_demo.websocket_demo
    import network_demo.applications
except ImportError:
    print("警告：无法导入部分网络编程演示模块")