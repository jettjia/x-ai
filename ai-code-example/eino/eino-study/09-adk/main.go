package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"os"

	"github.com/cloudwego/eino/adk"
	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"

	"github.com/cloudwego/eino-ext/components/model/openai"
)

// WeatherTool 天气查询工具结构体
type WeatherTool struct {
	apiKey string
}

// NewWeatherTool 创建天气查询工具实例
func NewWeatherTool(apiKey string) *WeatherTool {
	return &WeatherTool{
		apiKey: apiKey,
	}
}

// Info 返回工具信息
func (w *WeatherTool) Info(ctx context.Context) (*schema.ToolInfo, error) {
	return &schema.ToolInfo{
		Name: "get_weather",
		Desc: "获取指定城市和日期的天气信息。例如：get_weather(city='上海', extensions='base')",
		ParamsOneOf: schema.NewParamsOneOfByParams(map[string]*schema.ParameterInfo{
			"city": {
				Type:     schema.String,
				Required: true,
				Desc:     "城市名称",
			},
			"extensions": {
				Desc: "气象类型: base(实况天气) / all(预报天气)",
				Type: schema.String,
				Enum: []string{"base", "all"},
			},
		}),
	}, nil
}

// InvokableRun 执行天气查询
func (w *WeatherTool) InvokableRun(ctx context.Context, argumentsInJSON string, opts ...tool.Option) (string, error) {

	// 解析输入参数
	var params map[string]any
	if err := json.Unmarshal([]byte(argumentsInJSON), &params); err != nil {
		return "", fmt.Errorf("failed to parse input: %w", err)
	}

	city, ok := params["city"].(string)
	if !ok || city == "" {
		return "", fmt.Errorf("city is required")
	}

	// 构建API请求URL
	baseURL := "https://restapi.amap.com/v3/weather/weatherInfo"
	queryParams := url.Values{}
	queryParams.Set("city", city)
	queryParams.Set("key", w.apiKey)

	// 设置可选参数
	if extensions, ok := params["extensions"].(string); ok {
		queryParams.Set("extensions", extensions)
	} else {
		// 默认查询实况天气
		queryParams.Set("extensions", "base")
	}

	// 设置返回格式为JSON
	queryParams.Set("output", "JSON")

	fullURL := fmt.Sprintf("%s?%s", baseURL, queryParams.Encode())

	// 发送HTTP请求
	req, err := http.NewRequestWithContext(ctx, "GET", fullURL, nil)
	if err != nil {
		return "", fmt.Errorf("failed to create request: %w", err)
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", fmt.Errorf("failed to send request: %w", err)
	}
	defer resp.Body.Close()

	// 读取响应
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", fmt.Errorf("failed to read response: %w", err)
	}

	// 检查HTTP状态码
	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("API request failed with status %d: %s", resp.StatusCode, string(body))
	}

	return string(body), nil
}

func main() {
	ctx := context.Background()

	// 1. 初始化模型
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

	// 2. 创建天气查询工具（使用高德地图API）
	amapAPIKey := os.Getenv("AMAP_API_KEY")
	if amapAPIKey == "" {
		log.Fatal("AMAP_API_KEY environment variable is required")
	}
	weatherTool := NewWeatherTool(amapAPIKey)

	// 3. 绑定工具到模型
	info, err := weatherTool.Info(ctx)
	if err != nil {
		panic(err)
	}
	err = chatModel.BindTools([]*schema.ToolInfo{info})
	if err != nil {
		panic(err)
	}

	// 4. 创建天气查询Agent
	weatherAgent, err := adk.NewChatModelAgent(ctx, &adk.ChatModelAgentConfig{
		Name:        "weather_agent",
		Description: "天气查询智能助手，能够根据城市名称查询当前天气信息",
		Instruction: `
		你是一个专业的天气查询智能助手，你的职责是：
		1. 接收用户关于天气查询的请求
		2. 调用get_weather工具获取指定城市的天气信息
		3. 以友好、清晰的方式向用户展示天气信息
		4. 如果用户没有提供城市名称，默认查询上海的天气
		5. 你只能处理与天气相关的请求
		`,
		Model: chatModel,
		ToolsConfig: adk.ToolsConfig{
			ToolsNodeConfig: compose.ToolsNodeConfig{
				Tools: []tool.BaseTool{weatherTool},
				UnknownToolsHandler: func(ctx context.Context, name, input string) (string, error) {
					return fmt.Sprintf("未知工具: %s", name), nil
				},
			},
		},
		MaxIterations: 5, // 最大迭代次数
	})
	if err != nil {
		log.Fatal(err)
	}

	// 5. 创建Runner
	runner := adk.NewRunner(ctx, adk.RunnerConfig{
		Agent:           weatherAgent,
		EnableStreaming: true,
	})

	// 6. 执行对话
	fmt.Println("天气查询助手已启动")
	fmt.Println("正在查询上海的天气信息...")
	fmt.Println()

	// 默认查询上海的天气
	userInput := "上海"

	// 创建输入消息
	input := []adk.Message{
		schema.UserMessage(fmt.Sprintf("查询%s的天气", userInput)),
	}

	// 执行对话并流式输出
	fmt.Print("助手: ")
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
			// 流式输出消息内容
			fmt.Printf("%s", msg.Content)
		}
	}

	fmt.Println()
	fmt.Println()
	fmt.Println("天气查询完成！")
}
