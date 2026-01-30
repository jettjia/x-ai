package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/cloudwego/eino-ext/components/model/openai"
	"github.com/cloudwego/eino/components/prompt"
	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/components/tool/utils"
	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"
)

// 全局上下文，可根据业务替换为业务专属ctx
var globalCtx = context.Background()

func main() {
	// 1. 初始化所有依赖组件（模板/大模型/工具/自定义函数）
	chatTpl, err := initChatTemplate()
	if err != nil {
		log.Fatalf("初始化聊天模板失败: %v", err)
	}
	chatModel, err := initChatModel(globalCtx)
	if err != nil {
		log.Fatalf("初始化大模型客户端失败: %v", err)
	}
	toolsNode, toolInfos, err := initToolsNode(globalCtx)
	if err != nil {
		log.Fatalf("初始化工具节点失败: %v", err)
	}
	if err := chatModel.BindTools(toolInfos); err != nil {
		log.Fatalf("绑定工具到大模型失败: %v", err)
	}
	// 自定义Lambda函数：处理工具结果+行程规划结果的格式化
	takeOne := initLambdaConverter()

	// 2. 创建Graph工作流实例，泛型指定：
	// K: 输入输出数据类型（map[string]any，通用键值对）
	// V: 节点间传递的消息类型（*schema.Message，eino内置消息结构体）
	// 文档：NewGraph[K, V]() 初始化空的Graph工作流，无入参，返回*Graph[K, V]实例
	graphIns := compose.NewGraph[map[string]any, *schema.Message]()

	// 3. 向Graph中添加各类功能节点（核心执行单元，节点ID唯一）
	// 3.1 添加聊天模板节点：渲染Prompt模板，将用户输入填充为完整的大模型输入
	// 文档：AddChatTemplateNode(nodeID string, tpl *template.ChatTemplate) error
	// nodeID: 节点唯一标识（后续边/分支连接用），不可重复
	// tpl: 初始化后的聊天模板实例，包含Prompt模板和参数渲染规则
	if err := graphIns.AddChatTemplateNode("node_template", chatTpl); err != nil {
		log.Fatalf("添加模板节点失败: %v", err)
	}

	// 3.2 添加大模型节点：调用大模型API，处理渲染后的Prompt并返回响应
	// 文档：AddChatModelNode(nodeID string, m model.ChatModel) error
	// nodeID: 节点唯一标识
	// m: 初始化后的大模型客户端实例，已配置模型地址/APIKey/调用参数
	if err := graphIns.AddChatModelNode("node_model", chatModel); err != nil {
		log.Fatalf("添加大模型节点失败: %v", err)
	}

	// 3.3 添加工具执行节点：执行外部工具（此处为天气查询工具），处理大模型的工具调用指令
	// 文档：AddToolsNode(nodeID string, t *tool.ToolsNode) error
	// nodeID: 节点唯一标识
	// t: 初始化后的工具节点实例，已注册待执行的工具列表
	if err := graphIns.AddToolsNode("node_tools", toolsNode); err != nil {
		log.Fatalf("添加工具节点失败: %v", err)
	}

	// 3.4 添加Lambda自定义节点：对工具执行结果/大模型响应做自定义格式化处理
	// 文档：AddLambdaNode(nodeID string, f schema.LambdaFunc[V]) error
	// nodeID: 节点唯一标识
	// f: 自定义Lambda函数，签名需符合schema.LambdaFunc[V]（入参ctx+消息，出参消息+错误）
	if err := graphIns.AddLambdaNode("node_converter", takeOne); err != nil {
		log.Fatalf("添加Lambda节点失败: %v", err)
	}

	// 4. 定义节点执行关系（边=串行执行，分支=条件执行，从START开始到END结束）
	// 4.1 从虚拟入口节点START，串行执行模板节点（工作流第一步必渲染模板）
	// 文档：AddEdge(fromNodeID string, toNodeID string) error
	// fromNodeID: 源节点ID（可使用graph.START/GRAPH.END虚拟节点）
	// toNodeID: 目标节点ID（已定义的节点ID或虚拟节点）
	if err := graphIns.AddEdge(compose.START, "node_template"); err != nil {
		log.Fatalf("添加START→node_template边失败: %v", err)
	}

	// 4.2 模板节点执行完成后，串行执行大模型节点（渲染完直接调用大模型）
	if err := graphIns.AddEdge("node_template", "node_model"); err != nil {
		log.Fatalf("添加node_template→node_model边失败: %v", err)
	}

	// 4.3 大模型节点执行完成后，串行执行工具节点
	// 注意：在实际应用中，大模型会根据需要决定是否调用工具
	// 这里简化实现，直接连接到工具节点
	if err := graphIns.AddEdge("node_model", "node_tools"); err != nil {
		log.Fatalf("添加node_model→node_tools边失败: %v", err)
	}

	// 4.4 工具节点执行完成后，串行执行Lambda自定义节点（格式化工具结果+行程规划）
	if err := graphIns.AddEdge("node_tools", "node_converter"); err != nil {
		log.Fatalf("添加node_tools→node_converter边失败: %v", err)
	}

	// 4.5 Lambda节点执行完成后，走到虚拟出口节点END（工作流完成）
	if err := graphIns.AddEdge("node_converter", compose.END); err != nil {
		log.Fatalf("添加node_converter→END边失败: %v", err)
	}

	// 5. 编译Graph工作流（抽象流程→可执行流程，做合法性校验）
	// 文档：Compile(ctx context.Context) (*graph.CompiledGraph[K, V], error)
	// ctx: 上下文（传递超时/链路信息等）
	// 返回值1: 编译后的可执行工作流实例，提供Invoke方法执行
	// 返回值2: 编译错误（节点重复/边连接不存在/流程闭环等都会触发）
	compiledGraph, err := graphIns.Compile(globalCtx)
	if err != nil {
		log.Fatalf("编译Graph工作流失败: %v", err)
	}

	// 6. 调用执行编译后的工作流（传入用户输入，获取最终结果）
	// 文档：Invoke(ctx context.Context, input K) (K, error)
	// ctx: 上下文（可设置超时，如context.WithTimeout(globalCtx, 30*time.Second)）
	// input: 输入参数，类型与NewGraph的K泛型一致（此处为map[string]any）
	// 返回值1: 输出结果，类型与输入一致（封装了天气信息+行程规划）
	// 返回值2: 执行错误（某个节点执行失败/工具调用超时/大模型无响应等）
	input := map[string]any{
		"query": "查询上海未来3天的天气，然后规划一份3天的旅行行程", // 用户核心查询
		"city":  "上海",                        // 额外指定城市，方便模板/工具使用
		"days":  3,                           // 行程天数
	}
	// 设置30秒超时上下文，避免工作流执行卡死
	timeoutCtx, cancel := context.WithTimeout(globalCtx, 30*time.Second)
	defer cancel() // 延迟取消上下文，释放资源

	out, err := compiledGraph.Invoke(timeoutCtx, input)
	if err != nil {
		log.Fatalf("执行Graph工作流失败: %v", err)
	}

	// 7. 打印最终结果
	fmt.Println("==================== 上海天气+旅行行程规划结果 ====================")
	if out.ReasoningContent != "" {
		fmt.Println("【Reasoning】")
		fmt.Println(out.ReasoningContent)
	}
	fmt.Println(out.Content)
}

// ------------------------------ 初始化依赖组件：以下为业务专属实现，需根据实际环境调整 ------------------------------

// initChatTemplate 初始化聊天模板节点的模板配置
// 功能：将用户输入（city/days/query）填充到Prompt模板，生成大模型可识别的完整输入
// 返回：*template.ChatTemplate（eino内置模板实例）/错误
func initChatTemplate() (prompt.ChatTemplate, error) {
	// 定义Prompt模板，使用单花括号{XXX}语法渲染用户输入参数（与Invoke的input键一致）
	// 模板逻辑：1. 告诉大模型需要先判断是否有天气数据，无则调用天气工具；2. 有天气数据则规划行程；3. 结果结构化返回
	promptTpl := `
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
	// 初始化eino聊天模板，设置人类角色的模板内容（支持多轮对话，此处为单轮）
	// template.NewChatTemplate()：创建空模板实例
	// AddHumanTemplate(tpl string)：添加人类（用户）侧的模板（大模型的输入）
	chatTpl := prompt.FromMessages(schema.FString, schema.UserMessage(promptTpl))

	return chatTpl, nil
}

// initChatModel 初始化大模型客户端实例
// 功能：配置大模型的调用参数，提供大模型API调用能力（eino适配主流大模型，需根据实际使用的模型调整）
// 注意：需替换为实际的模型地址/APIKey/模型名称
// 返回：model.ChatModel（eino大模型接口实例）/错误
func initChatModel(ctx context.Context) (*openai.ChatModel, error) {
	// 以字节自研模型为例（替换为你实际使用的模型：如OpenAI/文心/通义，需引入对应客户端包）
	// 核心：实现eino的model.ChatModel接口（包含ChatCompletion(ctx context.Context, msg *schema.Message) (*schema.Message, error)方法）
	// 此处为简化实现，实际开发中需替换为真实的大模型客户端初始化代码
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
		return nil, fmt.Errorf("初始化OpenAI大模型客户端失败: %w", err)
	}
	return model, nil
}

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

// 注意：eino的graph目前不直接支持Branch接口，我们使用AddEdge来定义节点间的关系
// 对于需要条件分支的情况，我们可以在Lambda节点中处理逻辑
// 这里简化实现，直接连接节点
