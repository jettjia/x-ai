# -*- coding: utf-8 -*-

"""HTTP客户端编程示例

这个模块演示了如何使用Python的urllib和requests库发送HTTP请求。
"""

import urllib.request
import urllib.error


class UrllibHttpClient:
    """使用urllib模块的HTTP客户端"""
    
    def __init__(self):
        """初始化urllib HTTP客户端"""
        self.default_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def get(self, url, headers=None):
        """发送GET请求
        
        Args:
            url (str): 请求的URL地址
            headers (dict, optional): 请求头信息
            
        Returns:
            dict: 包含响应状态码、响应头和响应内容的字典
        """
        try:
            print(f"使用urllib请求URL: {url}")
            
            # 合并默认请求头和自定义请求头
            request_headers = self.default_headers.copy()
            if headers:
                request_headers.update(headers)
            
            # 创建请求对象
            request = urllib.request.Request(url, headers=request_headers)
            
            # 发送请求并获取响应
            with urllib.request.urlopen(request) as response:
                # 读取响应内容
                content = response.read().decode('utf-8')
                
                # 获取响应状态码
                status_code = response.status
                
                # 获取响应头
                headers = response.getheaders()
                
                print(f"响应状态码: {status_code}")
                print(f"响应头: {headers[:2]}...")  # 只打印前两个头信息
                print(f"响应内容长度: {len(content)} 字符")
                print(f"响应内容前100个字符: {content[:100]}...")
                
                return {
                    'status_code': status_code,
                    'headers': headers,
                    'content': content
                }
                
        except urllib.error.URLError as e:
            print(f"URL错误: {e}")
        except urllib.error.HTTPError as e:
            print(f"HTTP错误: 状态码 {e.code}, 原因: {e.reason}")
        except Exception as e:
            print(f"请求发生错误: {e}")
        
        return None


def get_requests_client():
    """尝试导入并返回requests客户端
    
    Returns:
        RequestsHttpClient or None: 如果安装了requests库，则返回RequestsHttpClient实例，否则返回None
    """
    try:
        import requests
        
        class RequestsHttpClient:
            """使用requests模块的HTTP客户端"""
            
            def __init__(self):
                """初始化requests HTTP客户端"""
                self.default_headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            
            def get(self, url, headers=None, params=None):
                """发送GET请求
                
                Args:
                    url (str): 请求的URL地址
                    headers (dict, optional): 请求头信息
                    params (dict, optional): URL参数
                    
                Returns:
                    dict: 包含响应状态码、响应头和响应内容的字典
                """
                try:
                    print(f"使用requests发送GET请求到URL: {url}")
                    
                    # 合并默认请求头和自定义请求头
                    request_headers = self.default_headers.copy()
                    if headers:
                        request_headers.update(headers)
                    
                    # 发送GET请求
                    response = requests.get(url, headers=request_headers, params=params)
                    
                    # 检查响应状态
                    response.raise_for_status()
                    
                    print(f"GET请求状态码: {response.status_code}")
                    print(f"响应头: {list(response.headers.items())[:2]}...")  # 只打印前两个头信息
                    print(f"响应内容长度: {len(response.text)} 字符")
                    
                    # 尝试解析JSON响应
                    result = {
                        'status_code': response.status_code,
                        'headers': dict(response.headers)
                    }
                    
                    if 'application/json' in response.headers.get('Content-Type', ''):
                        json_data = response.json()
                        print(f"GET请求JSON响应: {json_data}")
                        result['content'] = json_data
                    else:
                        result['content'] = response.text
                        print(f"GET请求文本响应前100个字符: {response.text[:100]}...")
                    
                    return result
                    
                except Exception as e:
                    print(f"GET请求发生错误: {e}")
                    return None
            
            def post(self, url, data=None, json=None, headers=None):
                """发送POST请求
                
                Args:
                    url (str): 请求的URL地址
                    data (dict, optional): 表单数据
                    json (dict, optional): JSON数据
                    headers (dict, optional): 请求头信息
                    
                Returns:
                    dict: 包含响应状态码、响应头和响应内容的字典
                """
                try:
                    print(f"使用requests发送POST请求到URL: {url}")
                    
                    # 合并默认请求头和自定义请求头
                    request_headers = self.default_headers.copy()
                    if headers:
                        request_headers.update(headers)
                    
                    # 发送POST请求
                    response = requests.post(url, data=data, json=json, headers=request_headers)
                    
                    # 检查响应状态
                    response.raise_for_status()
                    
                    print(f"POST请求状态码: {response.status_code}")
                    
                    # 尝试解析JSON响应
                    result = {
                        'status_code': response.status_code,
                        'headers': dict(response.headers)
                    }
                    
                    if 'application/json' in response.headers.get('Content-Type', ''):
                        json_data = response.json()
                        print(f"POST请求JSON响应: {json_data}")
                        result['content'] = json_data
                    else:
                        result['content'] = response.text
                    
                    return result
                    
                except Exception as e:
                    print(f"POST请求发生错误: {e}")
                    return None
        
        return RequestsHttpClient()
    except ImportError:
        print("未安装requests模块，请使用'pip install requests'命令安装")
        return None


def demo_http_clients():
    """演示HTTP客户端功能"""
    print("\n演示HTTP客户端功能:")
    
    # 测试URL
    test_url = "http://httpbin.org/get"
    
    # 使用urllib客户端
    print("\n1. 使用urllib模块发送GET请求:")
    urllib_client = UrllibHttpClient()
    urllib_client.get(test_url)
    
    # 尝试使用requests客户端
    print("\n2. 使用requests模块发送请求:")
    requests_client = get_requests_client()
    if requests_client:
        # 发送GET请求
        requests_client.get(test_url)
        
        # 发送带参数的GET请求
        print("\n发送带参数的GET请求:")
        params = {"page": 1, "limit": 10, "sort": "desc"}
        requests_client.get("http://httpbin.org/get", params=params)
        
        # 发送POST请求
        print("\n发送POST请求:")
        post_url = "http://httpbin.org/post"
        post_data = {"name": "张三", "age": 25, "city": "北京"}
        requests_client.post(post_url, json=post_data)


if __name__ == "__main__":
    # 当直接运行此模块时，演示HTTP客户端功能
    demo_http_clients()