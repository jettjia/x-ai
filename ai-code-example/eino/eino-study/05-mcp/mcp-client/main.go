package main

import (
	"context"
	"log"
	"os"

	"github.com/cloudwego/eino-ext/components/model/openai"
	mcpTool "github.com/cloudwego/eino-ext/components/tool/mcp"
	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/flow/agent/react"
	"github.com/cloudwego/eino/schema"
	"github.com/mark3labs/mcp-go/client"
	"github.com/mark3labs/mcp-go/mcp"
)

func main() {
	ctx := context.Background()
	// 初始化模型
	chatModel, err := openai.NewChatModel(ctx, &openai.ChatModelConfig{
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
	mcpTools, err := getMcpTools()
	if err != nil {
		panic(err)
	}
	agent, err := react.NewAgent(ctx, &react.AgentConfig{
		ToolCallingModel: chatModel,
		ToolsConfig: compose.ToolsNodeConfig{
			Tools: mcpTools,
		},
	})
	if err != nil {
		panic(err)
	}
	msg := []*schema.Message{
		schema.SystemMessage("请根据提供的天气查询工具，查询天气情况"),
		schema.UserMessage("查询北京今天的天气"),
	}
	result, err := agent.Generate(ctx, msg)
	if err != nil {
		panic(err)
	}

	println(result.Content)
}

func getMcpTools() ([]tool.BaseTool, error) {
	ctx := context.Background()
	// 创建SSE客户端连接到MCP服务器
	cli, err := client.NewSSEMCPClient("http://localhost:12345/sse")
	if err != nil {
		panic(err)
	}
	// 启动客户端
	err = cli.Start(ctx)
	if err != nil {
		panic(err)
	}
	initializeRequest := mcp.InitializeRequest{}
	initializeRequest.Params.ProtocolVersion = mcp.LATEST_PROTOCOL_VERSION
	initializeRequest.Params.ClientInfo = mcp.Implementation{
		Name:    "weather-tool",
		Version: "0.0.1",
	}
	_, err = cli.Initialize(ctx, initializeRequest)
	if err != nil {
		return nil, err
	}
	tools, err := mcpTool.GetTools(ctx, &mcpTool.Config{
		Cli: cli,
	})
	return tools, err
}
