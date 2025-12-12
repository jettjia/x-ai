package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/cloudwego/eino/adk"
	"github.com/cloudwego/eino/schema"

	"github.com/cloudwego/eino-ext/components/model/openai"
)

func main() {
	ctx := context.Background()

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
		log.Fatal(err)
	}

	// 创建 ChatModelAgent
	agent, err := adk.NewChatModelAgent(ctx, &adk.ChatModelAgentConfig{
		Name:        "hello_agent",
		Description: "友好的问候助理",
		Instruction: "你是个友好的助手。请用温暖的语气回应用户.",
		Model:       model,
	})
	if err != nil {
		log.Fatal(err)
	}

	// 创建 Runner
	runner := adk.NewRunner(ctx, adk.RunnerConfig{
		Agent:           agent,
		EnableStreaming: true,
	})

	// 执行对话
	input := []adk.Message{
		schema.UserMessage("你好，请自我介绍一下。"),
	}

	events := runner.Run(ctx, input)
	for {
		event, ok := events.Next()
		if !ok {
			break
		}

		if event.Err != nil {
			log.Printf("错误: %v", event.Err)
			break
		}

		if msg, err := event.Output.MessageOutput.GetMessage(); err == nil {
			fmt.Printf("Agent: %s\n", msg.Content)
		}
	}
}
