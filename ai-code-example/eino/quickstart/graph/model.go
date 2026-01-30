package main

import (
	"context"
	"fmt"
	"os"

	"github.com/cloudwego/eino-ext/components/model/openai"
)

// initChatModel 初始化大模型客户端实例
// 功能：配置大模型的调用参数，提供大模型API调用能力（eino适配主流大模型，需根据实际使用的模型调整）
// 注意：需替换为实际的模型地址/APIKey/模型名称
// 返回：model.ChatModel（eino大模型接口实例）/错误
func initChatModel(ctx context.Context) (*openai.ChatModel, error) {
	// 以字节自研模型为例（替换为你实际使用的模型：如OpenAI/文心/通义，需引入对应客户端包）
	// 核心：实现eino的model.ChatModel接口（包含ChatCompletion(ctx context.Context, msg *schema.Message) (*schema.Message, error)方法）
	// 此处为简化实现，实际开发中需替换为真实的大模型客户端初始化代码
	// 初始化模型
	model, err := openai.NewChatModel(ctx, &openai.ChatModelConfig{
		APIKey:  os.Getenv("OPENAI_API_KEY"),
		Model:   os.Getenv("OPENAI_MODEL"),
		BaseURL: os.Getenv("OPENAI_BASE_URL"),
		ByAzure: func() bool {
			return os.Getenv("OPENAI_BY_AZURE") == "true"
		}(),
	})
	if err != nil {
		return nil, fmt.Errorf("初始化OpenAI大模型客户端失败: %w", err)
	}
	return model, nil
}
