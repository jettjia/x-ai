package main

import (
	"context"
	"encoding/json"
	"fmt"
	"strings"
	"time"

	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"
)

// 修改Lambda函数的实现，使其能够处理消息数组类型的输入
func initLambdaConverter() *compose.Lambda {
	// 定义Lambda函数，入参：ctx（上下文）、msg（上一个节点传递的消息，此处为工具节点的执行结果，类型为[]*schema.Message）
	// 出参：*schema.Message（处理后的消息，传递给END）、error（处理错误）
	transformOps := func(ctx context.Context, input *schema.StreamReader[[]*schema.Message]) (output *schema.StreamReader[*schema.Message], err error) {
		return schema.StreamReaderWithConvert(input, func(input []*schema.Message) (output *schema.Message, err error) {
			type weatherItem struct {
				Date    string `json:"date"`
				Weather string `json:"weather"`
				Temp    string `json:"temp"`
				Wind    string `json:"wind"`
			}
			type weatherData struct {
				City string        `json:"city"`
				Days int           `json:"days"`
				List []weatherItem `json:"list"`
			}

			// 1. 检查输入消息数组是否为空
			if len(input) == 0 {
				return nil, fmt.Errorf("工具节点输出消息为空")
			}

			// 2. 取第一个消息作为处理对象（通常工具节点只返回一个消息）
			toolMessage := input[0]

			// 3. 解析工具执行的天气数据
			var weatherResult weatherData
			if err := json.Unmarshal([]byte(toolMessage.Content), &weatherResult); err != nil {
				return nil, fmt.Errorf("解析天气工具结果失败: %w", err)
			}
			if len(weatherResult.List) < 3 {
				return nil, fmt.Errorf("天气工具结果天数不足，实际=%d", len(weatherResult.List))
			}

			// 4. 模拟大模型基于天气数据生成的行程规划
			travelPlan := map[string]any{
				"day1": map[string]any{
					"date":    weatherResult.List[0].Date,
					"weather": weatherResult.List[0].Weather,
					"scenic":  "上海迪士尼乐园（晴适合户外活动）",
					"traffic": "地铁11号线直达",
					"food":    "迪士尼小镇网红小吃（火鸡腿、米奇冰淇淋）",
				},
				"day2": map[string]any{
					"date":    weatherResult.List[1].Date,
					"weather": weatherResult.List[1].Weather,
					"scenic":  "外滩+南京路步行街（多云适合散步）",
					"traffic": "地铁2号线南京东路站",
					"food":    "南京路生煎包+外滩本帮菜（老正兴）",
				},
				"day3": map[string]any{
					"date":    weatherResult.List[2].Date,
					"weather": weatherResult.List[2].Weather,
					"scenic":  "上海豫园+城隍庙（晴间多云适合逛园林）",
					"traffic": "地铁10号线豫园站",
					"food":    "城隍庙南翔小笼包+梨膏糖",
				},
			}

			// 5. 构造最终的结构化结果
			finalResult := map[string]any{
				"weather_info": weatherResult,                            // 上海未来3天天气信息
				"travel_plan":  travelPlan,                               // 3天旅行行程规划
				"tips":         "上海近期气温适中，建议携带薄外套，晴好天气注意防晒",              // 旅行小贴士
				"update_time":  time.Now().Format("2006-01-02 15:04:05"), // 结果更新时间
			}

			// 6. 将最终结果序列化为JSON字符串
			resultJson, err := json.MarshalIndent(finalResult, "", "  ")
			if err != nil {
				return nil, fmt.Errorf("序列化最终结果失败: %w", err)
			}

			// 7. 创建新的消息并返回
			return &schema.Message{
				Content: string(resultJson),
			}, nil
		}), nil
	}
	return compose.TransformableLambda[[]*schema.Message, *schema.Message](transformOps)
}

func initDirectConverter() *compose.Lambda {
	transformOps := func(ctx context.Context, input *schema.StreamReader[*schema.Message]) (output *schema.StreamReader[*schema.Message], err error) {
		return schema.StreamReaderWithConvert(input, func(input *schema.Message) (output *schema.Message, err error) {
			if input == nil {
				return nil, fmt.Errorf("大模型输出为空")
			}

			cleaned := strings.TrimSpace(input.Content)
			if strings.HasPrefix(cleaned, "```") {
				lines := strings.Split(cleaned, "\n")
				if len(lines) >= 3 {
					if strings.HasPrefix(strings.TrimSpace(lines[0]), "```") {
						lines = lines[1:]
					}
					last := len(lines) - 1
					if strings.TrimSpace(lines[last]) == "```" {
						lines = lines[:last]
					}
					cleaned = strings.TrimSpace(strings.Join(lines, "\n"))
				}
			}

			var parsed any
			if err := json.Unmarshal([]byte(cleaned), &parsed); err == nil {
				b, err := json.MarshalIndent(parsed, "", "  ")
				if err != nil {
					return nil, err
				}
				return &schema.Message{Content: string(b)}, nil
			}

			finalResult := map[string]any{
				"model_output": input.Content,
				"update_time":  time.Now().Format("2006-01-02 15:04:05"),
			}
			b, err := json.MarshalIndent(finalResult, "", "  ")
			if err != nil {
				return nil, err
			}
			return &schema.Message{Content: string(b)}, nil
		}), nil
	}
	return compose.TransformableLambda[*schema.Message, *schema.Message](transformOps)
}
