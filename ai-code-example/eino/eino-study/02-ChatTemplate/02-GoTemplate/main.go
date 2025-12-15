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
		schema.GoTemplate,
		schema.SystemMessage("{{if .isExpert}}你是一个专家级{{.domain}}顾问。{{else}}你是一个初级{{.domain}}助手。{{end}}\n{{if .isFormal}}请使用正式的语言风格。{{else}}请使用友好的语言风格。{{end}}\n你的任务是{{.task}}。"),
		schema.UserMessage("{{.question}}"),
	)
	//vars := map[string]any{
	//	"isExpert": true,
	//	"domain":   "数据库",
	//	"isFormal": true,
	//	"task":     "提供专业的数据库优化建议",
	//	"question": "如何优化大型数据库的查询性能？",
	//}
	vars := map[string]interface{}{
		"isExpert": false,
		"domain":   "编程",
		"isFormal": false,
		"task":     "帮助初学者理解编程概念",
		"question": "什么是变量？",
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
