package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"
)

// 全局上下文，可根据业务替换为业务专属ctx
var globalCtx = context.Background()

func main() {
	// 1. 初始化所有依赖组件（模板/大模型/工具/自定义函数）
	weatherChatTpl, directChatTpl, err := initChatTemplates()
	if err != nil {
		log.Fatalf("初始化聊天模板失败: %v", err)
	}
	weatherChatModel, err := initChatModel(globalCtx)
	if err != nil {
		log.Fatalf("初始化大模型客户端失败: %v", err)
	}
	directChatModel, err := initChatModel(globalCtx)
	if err != nil {
		log.Fatalf("初始化大模型客户端失败: %v", err)
	}
	toolsNode, toolInfos, err := initToolsNode(globalCtx)
	if err != nil {
		log.Fatalf("初始化工具节点失败: %v", err)
	}
	if err := weatherChatModel.BindTools(toolInfos); err != nil {
		log.Fatalf("绑定工具到大模型失败: %v", err)
	}
	// 自定义Lambda函数：处理工具结果+行程规划结果的格式化
	takeOne := initLambdaConverter()
	directConverter := initDirectConverter()

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
	if err := graphIns.AddChatTemplateNode("node_template_weather", weatherChatTpl); err != nil {
		log.Fatalf("添加模板节点失败: %v", err)
	}
	if err := graphIns.AddChatTemplateNode("node_template_direct", directChatTpl); err != nil {
		log.Fatalf("添加模板节点失败: %v", err)
	}

	// 3.2 添加大模型节点：调用大模型API，处理渲染后的Prompt并返回响应
	// 文档：AddChatModelNode(nodeID string, m model.ChatModel) error
	// nodeID: 节点唯一标识
	// m: 初始化后的大模型客户端实例，已配置模型地址/APIKey/调用参数
	if err := graphIns.AddChatModelNode("node_model_weather", weatherChatModel); err != nil {
		log.Fatalf("添加大模型节点失败: %v", err)
	}
	if err := graphIns.AddChatModelNode("node_model_direct", directChatModel); err != nil {
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
	if err := graphIns.AddLambdaNode("node_direct_converter", directConverter); err != nil {
		log.Fatalf("添加Lambda节点失败: %v", err)
	}

	// 4. 定义节点执行关系（边=串行执行，分支=条件执行，从START开始到END结束）
	// 4.1 从虚拟入口节点START，串行执行模板节点（工作流第一步必渲染模板）
	// 文档：AddEdge(fromNodeID string, toNodeID string) error
	// fromNodeID: 源节点ID（可使用graph.START/GRAPH.END虚拟节点）
	// toNodeID: 目标节点ID（已定义的节点ID或虚拟节点）
	startBranch := compose.NewGraphBranch(func(ctx context.Context, in map[string]any) (endNode string, err error) {
		if v, ok := in["need_weather"].(bool); ok && !v {
			return "node_template_direct", nil
		}
		return "node_template_weather", nil
	}, map[string]bool{
		"node_template_weather": true,
		"node_template_direct":  true,
	})
	if err := graphIns.AddBranch(compose.START, startBranch); err != nil {
		log.Fatalf("添加START分支失败: %v", err)
	}

	// 4.2 模板节点执行完成后，串行执行大模型节点（渲染完直接调用大模型）
	if err := graphIns.AddEdge("node_template_weather", "node_model_weather"); err != nil {
		log.Fatalf("添加node_template→node_model边失败: %v", err)
	}
	if err := graphIns.AddEdge("node_template_direct", "node_model_direct"); err != nil {
		log.Fatalf("添加node_template→node_model边失败: %v", err)
	}

	// 4.3 大模型节点执行完成后，串行执行工具节点
	// 注意：在实际应用中，大模型会根据需要决定是否调用工具
	// 这里简化实现，直接连接到工具节点
	if err := graphIns.AddEdge("node_model_weather", "node_tools"); err != nil {
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
	if err := graphIns.AddEdge("node_model_direct", "node_direct_converter"); err != nil {
		log.Fatalf("添加node_model→node_direct_converter边失败: %v", err)
	}
	if err := graphIns.AddEdge("node_direct_converter", compose.END); err != nil {
		log.Fatalf("添加node_direct_converter→END边失败: %v", err)
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
	testInputs := []map[string]any{
		{
			"query":        "查询上海未来3天的天气，然后规划一份3天的旅行行程",
			"city":         "上海",
			"days":         3,
			"need_weather": true,
		},
		{
			"query":        "不需要天气数据，直接给我一份3天旅行行程",
			"city":         "上海",
			"days":         3,
			"need_weather": false,
		},
	}
	for _, input := range testInputs {
		// 设置30秒超时上下文，避免工作流执行卡死
		timeoutCtx, cancel := context.WithTimeout(globalCtx, 30*time.Second)
		out, err := compiledGraph.Invoke(timeoutCtx, input)
		cancel()
		if err != nil {
			log.Fatalf("执行Graph工作流失败: %v", err)
		}

		fmt.Println("==================== Graph 输出 ====================")
		fmt.Printf("need_weather=%v\n", input["need_weather"])
		if out.ReasoningContent != "" {
			fmt.Println("【Reasoning】")
			fmt.Println(out.ReasoningContent)
		}
		fmt.Println(out.Content)
	}
}
