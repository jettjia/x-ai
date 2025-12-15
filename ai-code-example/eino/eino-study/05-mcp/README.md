# MCP (Model Context Protocol)

MCP (Model Context Protocol) 是一种标准化协议，允许语言模型与外部工具和服务进行交互。通过 MCP，模型可以：

访问文件系统
执行命令行操作
调用外部 API
与其他服务进行交互

# MCP Tool
在https://github.com/cloudwego/eino-ext项目中的components/tool/mcp中实现了一个MCP Tool，能够与Eino框架的工具系统轻松集成，支持获取和调用MCP工具

## 安装
```go
go get github.com/cloudwego/eino-ext/components/tool/mcp@latest
go get github.com/mark3labs/mcp-go
```
