package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"

	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/schema"
)

type WeatherTool struct {
	apiKey string
}

func NewWeatherTool(apiKey string) *WeatherTool {
	return &WeatherTool{
		apiKey: apiKey,
	}
}

func (w *WeatherTool) Info(ctx context.Context) (*schema.ToolInfo, error) {
	return &schema.ToolInfo{
		Name: "get_weather",
		Desc: "获取指定城市和日期的天气信息。例如：get_weather(city='北京', extensions='base')",
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
