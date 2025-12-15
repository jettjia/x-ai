package main

import (
	"context"
	"log"
	"os"

	"github.com/cloudwego/eino-ext/components/model/openai"
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

	message := []*schema.Message{
		schema.SystemMessage("你是一个乐于助人的助手"),
		schema.UserMessage("请介绍一下Go语言的特点"),
	}

	// Generate，一次性生成响应
	// response, err := model.Generate(ctx, message)
	// if err != nil {
	// 	panic(err)
	// }
	// println("model: ", response.Content)

	// Stream，流式生成响应
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
