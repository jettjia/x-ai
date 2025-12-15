工具调用
AI模型虽然很聪明，但它无法直接获取实时信息或执行具体操作。通过工具调用，我们可以让AI"借用"其他程序的能力，比如查询天气、搜索网页等。

# 1. ToolsNode组件
ToolsNode是Eino框架中的一个核心组件，它允许AI模型调用外部工具来扩展其能力。可以把它想象成一个工具箱，AI模型可以通过这个工具箱使用各种工具来完成特定任务。

在现实生活中，即使是再聪明的人，也需要借助工具来完成某些专业任务。比如：

医生需要使用听诊器、X光机等设备来诊断病情
工程师需要使用各种专业工具来设计和建造建筑
程序员需要使用IDE、调试工具等来编写代码
## 1.1 好处
使用ToolsNode组件有以下优势：

标准化接口：所有工具都遵循统一的接口规范，便于集成和管理
灵活扩展：可以轻松添加新的工具实现
易于使用：通过简单的配置即可使用各种工具
统一管理：可以集中管理所有工具的调用和配置
## 1.2 接口
ToolsNode主要实现了三个接口：

### 1.2.1 BaseTool
BaseTool是所有工具的基础接口，提供工具的基本信息：

type BaseTool interface {
    Info(ctx context.Context) (*schema.ToolInfo, error)
}
ToolInfo结构体包含了工具的描述信息，这些信息会提供给大模型，帮助它了解如何使用这个工具：

type ToolInfo struct {
    // 工具的唯一名称，用于清晰地表达其用途
    Name string
    // 用于告诉模型如何/何时/为什么使用这个工具
    // 可以在描述中包含少量示例
    Desc string
    // 工具接受的参数定义
    *ParamsOneOf
}
### 1.2.2 InvokableTool
InvokableTool是支持同步调用的工具接口：

type InvokableTool interface {
    BaseTool
    InvokableRun(ctx context.Context, argumentsInJSON string, opts ...Option) (string, error)
}
### 1.2.3 StreamableTool
StreamableTool是支持流式输出的工具接口：

type StreamableTool interface {
    BaseTool
    StreamableRun(ctx context.Context, argumentsInJSON string, opts ...Option) (*schema.StreamReader[string], error)
}
## 1.3 工作原理
创建工具集，将工具注册到ToolsNode中
将工具的信息ToolInfo告诉大模型
收到来自ChatModel组件的输出，其中一般会包含要调用的工具名称和参数
ToolsNode会在已注册的工具列表中找到对应的工具实现
执行工具调用，调用工具的InvokableRun或StreamableRun方法
最后将工具的调用结果封装为Message消息返回

# 2. 实际案例
## 2.1 查询天气
如果我们让大模型查询一下当前的天气情况或者未来几天的天气情况，大模型是做不到这件事情的，因为它的知识来自于它训练的数据集，它的记忆截止于训练完成的那一刻。

如果想要让大模型能够具备查询天气的功能，我们需要提供一个查询天气的工具，然后将工具的描述信息，告诉大模型，这样当大模型接到你要查询天气的请求时，他就会知道，有一个工具可以帮助我做到这件事情，从而调用工具，获取天气结果，最后给用户一个准确的回答。

1.首先定义一个天气查询的工具，主要就是实现上述，我们讲的三个接口(这里的实现，我们使用的是高德天气查询，这里你可以替换为其他的天气API)

2.创建一个ToolsNode，将天气工具添加进Tools列表中

3.模拟一个tool call的调用信息，然后调用toolsNode，检查工具调用的结果

4.如果要和 ChatModel 共同使用，即 ChatModel 产生tool call调用指令，Eino解析tool call指令来调用 ToolsNode, 需要调用 ChatModel 的 WithTools() 函数将工具描述信息传递给大模型。
