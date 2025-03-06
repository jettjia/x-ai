package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/tmc/langchaingo/llms"
	"github.com/tmc/langchaingo/llms/openai"
)

func main() {
	// 设置 OpenAI API 密钥
	apiKey := os.Getenv("OPENAI_API_KEY")
	// 创建 OpenAI 客户端
	llm, err := openai.New(
		openai.WithToken(apiKey),
		openai.WithModel("gpt-4o"),
	)
	if err != nil {
		log.Fatalf("Failed to create OpenAI LLM: %v", err)
	}

	ctx := context.Background()
	completion, err := llm.Call(ctx, "The first man to walk on the moon",
		llms.WithTemperature(0.8),
		llms.WithStopWords([]string{"Armstrong"}),
	)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(completion)
}
