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
		schema.FString,
		schema.SystemMessage("你是一个{role}, 请用{tone}的语气回答问题"),
		schema.UserMessage("{question}"),
	)
	vars := map[string]any{
		"role":     "技术专家",
		"tone":     "专业严谨",
		"question": "如何优化数据库性能",
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
