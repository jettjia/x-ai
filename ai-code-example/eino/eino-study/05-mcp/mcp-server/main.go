package main

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"

	"github.com/mark3labs/mcp-go/mcp"
	"github.com/mark3labs/mcp-go/server"
)

func main() {
	mcpServer := server.NewMCPServer("weather", mcp.LATEST_PROTOCOL_VERSION)
	tool := WeatherTool()
	mcpServer.AddTool(tool, func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		//解析输入参数
		params := request.GetArguments()
		city, ok := params["city"].(string)
		if !ok || city == "" {
			return nil, fmt.Errorf("city is required")
		}
		//构建API请求URL
		baseURL := "https://restapi.amap.com/v3/weather/weatherInfo"
		queryParams := url.Values{}
		queryParams.Set("city", city)
		queryParams.Set("key", os.Getenv("AMAP_API_KEY"))
		//设置可选参数
		if extensions, ok := params["extensions"].(string); ok {
			queryParams.Set("extensions", extensions)
		} else {
			// 默认查询实况天气
			queryParams.Set("extensions", "base")
		}
		//设置返回格式为JSON
		queryParams.Set("output", "JSON")
		fullURL := fmt.Sprintf("%s?%s", baseURL, queryParams.Encode())
		//发送HTTP请求
		req, err := http.NewRequestWithContext(ctx, "GET", fullURL, nil)
		if err != nil {
			return nil, fmt.Errorf("failed to create request: %w", err)
		}
		client := &http.Client{}
		resp, err := client.Do(req)
		if err != nil {
			return nil, fmt.Errorf("failed to send request: %w", err)
		}
		defer resp.Body.Close()
		//读取响应
		body, err := io.ReadAll(resp.Body)
		if err != nil {
			return nil, fmt.Errorf("failed to read response: %w", err)
		}
		//检查HTTP状态码
		if resp.StatusCode != http.StatusOK {
			return nil, fmt.Errorf("API request failed with status %d: %s", resp.StatusCode, string(body))
		}
		return mcp.NewToolResultText(string(body)), nil
	})

	err := server.NewSSEServer(mcpServer).Start("localhost:12345")
	if err != nil {
		panic(err)
	}
}

func WeatherTool() mcp.Tool {
	tool := mcp.NewTool("get_weather",
		mcp.WithDescription("Get weather information for a given city"),
		mcp.WithString("city", mcp.Required(), mcp.Description("城市名称")),
		mcp.WithString("extensions",
			mcp.Required(),
			mcp.Enum("base", "all"),
			mcp.Description("返回数据类型，base为实况天气，all为预报天气"),
			mcp.DefaultString("base"),
		),
	)
	return tool
}
