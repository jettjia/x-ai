package main

import (
	"github.com/cloudwego/eino/components/prompt"
	"github.com/cloudwego/eino/schema"
)

// initChatTemplate 初始化聊天模板节点的模板配置
// 功能：将用户输入（city/days/query）填充到Prompt模板，生成大模型可识别的完整输入
// 返回：*template.ChatTemplate（eino内置模板实例）/错误
func initChatTemplates() (prompt.ChatTemplate, prompt.ChatTemplate, error) {
	weatherPromptTpl := `
你是一名专业的旅行规划师，需要完成用户的需求：{query}
执行规则：
1. 首先检查你是否拥有{city}未来{days}天的精准天气数据（含日期/天气状况/气温/风力）；
2. 若没有天气数据，**必须调用**「weather_query」工具获取天气信息，工具入参为：city={city}，days={days}；
3. 若有天气数据，结合天气情况为{city}规划{days}天的旅行行程，要求：
   - 行程包含「日期/天气适配的景点/交通方式/美食推荐」；
   - 行程节奏适中，避免过于紧凑；
   - 结果按JSON格式返回，键为"weather_info"（天气信息）和"travel_plan"（行程规划）；
4. 必须使用工具调用能力触发工具执行，不要用纯文本编造工具结果。
`
	directPromptTpl := `
你是一名专业的旅行规划师，需要完成用户的需求：{query}
要求：
1. 不要调用任何工具；
2. 直接为{city}规划{days}天旅行行程；
3. 结果按JSON格式返回，键为"travel_plan"和"tips"。
`
	weatherChatTpl := prompt.FromMessages(schema.FString, schema.UserMessage(weatherPromptTpl))
	directChatTpl := prompt.FromMessages(schema.FString, schema.UserMessage(directPromptTpl))
	return weatherChatTpl, directChatTpl, nil
}
