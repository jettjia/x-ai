package main

import (
	"context"
	"log"
	"os"

	"github.com/cloudwego/eino-ext/components/model/qwen"
	"github.com/cloudwego/eino/components/model"
)

func createQwenChatModel(ctx context.Context) model.ChatModel {
	apiKey := os.Getenv("DASHSCOPE_API_KEY")
	chatModel, err := qwen.NewChatModel(ctx, &qwen.ChatModelConfig{
		BaseURL:     "https://dashscope.aliyuncs.com/compatible-mode/v1",
		APIKey:      apiKey,
		Timeout:     0,
		Model:       "qwen-max",
		MaxTokens:   of(2048),
		Temperature: of(float32(0.7)),
		TopP:        of(float32(0.7)),
	})

	if err != nil {
		log.Fatalf("create qwen chat model failed, err=%v", err)
	}
	return chatModel
}

func of[T any](t T) *T {
	return &t
}
