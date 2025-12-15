package main

import (
	"context"
	"log"
	"os"

	"github.com/cloudwego/eino-ext/components/model/openai"
	"github.com/cloudwego/eino/components/prompt"
	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"
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

	// tool
	weatherTool := NewWeatherTool(os.Getenv("AMAP_API_KEY")) // 导入tool
	//创建ToolsNode
	toolNode, err := compose.NewToolNode(ctx, &compose.ToolsNodeConfig{
		Tools: []tool.BaseTool{weatherTool},
	})
	if err != nil {
		panic(err)
	}
	weatherInfo, err := weatherTool.Info(ctx)
	if err != nil {
		panic(err)
	}

	// 绑定工具到模型
	toolCallingChatModel, err := model.WithTools([]*schema.ToolInfo{
		weatherInfo,
	})
	if err != nil {
		panic(err)
	}
	messages := prompt.FromMessages(schema.GoTemplate,
		schema.SystemMessage("你是一个AI助手，你必须调用工具来获取天气信息"),
		schema.UserMessage("我需要查询北京今天的天气"),
	)

	vars := map[string]any{}
	result, err := messages.Format(ctx, vars)
	if err != nil {
		panic(err)
	}

	input, err := toolCallingChatModel.Generate(ctx, result)
	if err != nil {
		panic(err)
	}
	println(input.Content)
	for _, v := range input.ToolCalls {
		println("=======================")
		println(v.Function.Name)
		println(v.Function.Arguments)
	}

	toolMessage, err := toolNode.Invoke(ctx, input)
	if err != nil {
		panic(err)
	}
	for _, v := range toolMessage {
		println(v.Content)
	}
}
