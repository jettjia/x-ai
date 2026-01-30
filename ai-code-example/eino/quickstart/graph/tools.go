package main

import (
	"context"
	"fmt"
	"time"

	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/components/tool/utils"
	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"
)

// initToolsNode 初始化工具节点，注册天气查询工具
// 功能：将「天气查询工具」注册到eino的工具节点，大模型调用工具时自动执行
// 返回：*tool.ToolsNode（eino工具节点实例）/错误
func initToolsNode(ctx context.Context) (*compose.ToolsNode, []*schema.ToolInfo, error) {

	getWeather, err := utils.InferTool(
		"weather_query",
		"this tool can query the weather of the specific city for the next N days",
		weatherQueryTool,
	)
	if err != nil {
		return nil, nil, err
	}

	info, err := getWeather.Info(ctx)
	if err != nil {
		return nil, nil, err
	}

	tools := []tool.BaseTool{
		getWeather,
	}
	// 1. 创建工具节点实例
	toolsNode, err := compose.NewToolNode(ctx, &compose.ToolsNodeConfig{
		Tools: tools,
	})
	if err != nil {
		return nil, nil, fmt.Errorf("创建工具节点失败: %w", err)
	}

	return toolsNode, []*schema.ToolInfo{info}, nil
}

// weatherQueryTool 天气查询工具的实际执行函数（业务核心）
// 功能：调用外部天气API，查询指定城市未来N天的天气数据（此处为模拟实现，实际需替换为真实API）
// 入参：ctx（上下文）、params（工具参数，大模型传递的{"city":"上海","days":3}）
// 出参：结构化天气数据/错误
func weatherQueryTool(ctx context.Context, params map[string]any) (any, error) {
	// 1. 解析工具参数（做类型校验，避免参数错误）
	city, ok := params["city"].(string)
	if !ok || city == "" {
		return nil, fmt.Errorf("工具参数city无效，值：%v", params["city"])
	}
	days, ok := params["days"].(float64) // JSON解析的数字默认是float64，需转换
	if !ok || days <= 0 {
		return nil, fmt.Errorf("工具参数days无效，值：%v", params["days"])
	}

	// 2. 模拟调用外部天气API（实际开发中替换为真实的天气API调用，如高德/百度/心知天气）
	// 结构化返回天气数据：日期/天气状况/气温/风力
	weatherData := map[string]any{
		"city": city,
		"days": int(days),
		"list": []map[string]any{
			{"date": time.Now().Add(24 * time.Hour).Format("2006-01-02"), "weather": "晴", "temp": "8~18℃", "wind": "东北风2级"},
			{"date": time.Now().Add(48 * time.Hour).Format("2006-01-02"), "weather": "多云转晴", "temp": "9~19℃", "wind": "东风1级"},
			{"date": time.Now().Add(72 * time.Hour).Format("2006-01-02"), "weather": "晴间多云", "temp": "7~17℃", "wind": "西北风2级"},
		},
	}

	// 3. 返回工具执行结果（eino会自动将结果封装成schema.Message，传递给下一个节点）
	return weatherData, nil
}
