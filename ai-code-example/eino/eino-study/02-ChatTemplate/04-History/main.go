package main

import (
	"context"
	"fmt"
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
		schema.GoTemplate,
		schema.SystemMessage(`你是一个{{.role}}，你的任务是{{.task}}。
请参考之前的对话历史来回答当前的问题`),
		schema.MessagesPlaceholder("history", false),
		schema.UserMessage("{{.question}}"),
	)
	vars := map[string]any{
		"role": "记忆器",
		"task": "根据用户提供的信息，给出准确的回答，如果历史中有答案，采用用户的答案",
		"history": []*schema.Message{
			schema.UserMessage("你好，我想了解一下Go语言的并发机制"),
			schema.AssistantMessage("Go语言提供了goroutines和channels来支持并发编程。Goroutines是轻量级线程，channels用于goroutines之间的通信。", nil),
			schema.UserMessage("你错了，Go语言只提供了go关键字来支持并发"),
		},
		"question": "Go语言的并发机制",
	}
	message, err := template.Format(ctx, vars)
	if err != nil {
		panic(err)
	}

	for _, v := range message {
		println(v.Content)
	}
	fmt.Println("===============================\n")

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
