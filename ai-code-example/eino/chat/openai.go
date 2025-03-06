package main

import (
	"context"
	"log"
	"os"

	"github.com/cloudwego/eino-ext/components/model/openai"
	"github.com/cloudwego/eino/components/model"
)

func createOpenAIChatModel(ctx context.Context) model.ChatModel {
	key := os.Getenv("OPENAI_API_KEY")
	chatModel, err := openai.NewChatModel(ctx, &openai.ChatModelConfig{
		Model:  "gpt-4o", // 使用的模型版本
		APIKey: key,      // OpenAI API 密钥
	})
	if err != nil {
		log.Fatalf("create openai chat model failed, err=%v", err)
	}
	return chatModel
}
