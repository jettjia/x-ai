package main

import (
	"context"
	"log"
	"os"

	"github.com/cloudwego/eino-ext/components/model/openai"
	"github.com/cloudwego/eino/components/prompt"
	"github.com/cloudwego/eino/schema"
)

func main() {
	// 初始化模型
	ctx := context.Background()
	model, err := openai.NewChatModel(ctx, &openai.ChatModelConfig{
		APIKey:  os.Getenv("OPENAI_API_KEY"),
		Model:   os.Getenv("OPENAI_MODEL"),
		BaseURL: os.Getenv("OPENAI_BASE_URL"),
		ByAzure: func() bool {
			return os.Getenv("OPENAI_BY_AZURE") == "true"
		}(),
	})
	if err != nil {
		log.Fatal(err)
	}

	template := prompt.FromMessages(
		schema.Jinja2,
		schema.SystemMessage(`{% if level == 'expert' %}你是一个专家级顾问。{% else %}你是一个初级助手。{% endif %}
{% if domain %}你专长于{{ domain }}领域。{% endif %}
请用{% if formal %}正式{% else %}友好{% endif %}的语气回答问题。`),
		schema.UserMessage("{{question}}"),
	)

	vars := map[string]any{
		"level":    "expert",
		"domain":   "人工智能",
		"formal":   true,
		"question": "请解释Transformer模型的工作原理。",
	}
	message, err := template.Format(ctx, vars)
	if err != nil {
		panic(err)
	}

	//获取流式回复
	stream, err := model.Stream(ctx, message)
	if err != nil {
		panic(err)
	}
	defer stream.Close()

	for {
		chunk, err := stream.Recv()
		if err != nil {
			break
		}
		print(chunk.Content)
	}
}
