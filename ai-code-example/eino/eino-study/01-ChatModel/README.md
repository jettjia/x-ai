# ChatModel 组件
doc: https://www.cloudwego.io/zh/docs/eino/core_modules/components/chat_model_guide/

Model 组件是一个用于与大语言模型交互的组件。它的主要作用是将用户的输入消息发送给语言模型，并获取模型的响应。这个组件在以下场景中发挥重要作用：

自然语言对话
文本生成和补全
工具调用的参数生成
多模态交互（文本、图片、音频等）


# 接口定义
```go
type BaseChatModel interface {
    Generate(ctx context.Context, input []*schema.Message, opts ...Option) (*schema.Message, error)
    Stream(ctx context.Context, input []*schema.Message, opts ...Option) (
        *schema.StreamReader[*schema.Message], error)
}

type ToolCallingChatModel interface {
    BaseChatModel

    // WithTools returns a new ToolCallingChatModel instance with the specified tools bound.
    // This method does not modify the current instance, making it safer for concurrent use.
    WithTools(tools []*schema.ToolInfo) (ToolCallingChatModel, error)
}

```