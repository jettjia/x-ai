# Agent

在AI应用开发中，Agent（智能体）是一种能够自主决策、执行任务并与环境交互的程序。

理解用户需求：分析用户输入的问题或指令
制定行动计划：决定需要执行哪些步骤来完成任务
调用工具：使用各种工具获取信息或执行操作
生成结果：整合所有信息，给出最终答案

Eino框架提供了强大的Agent支持，包括ReAct Agent和Multi-Agent两种主要类型。

# ReAct Agent
ReAct Agent是一种基于ReAct（Reasoning and Acting）框架的Agent。它能够理解用户指令，通过调用工具获取信息，并根据信息生成最终答案。

ReAct Agent的工作流程如下：

接收用户输入：获取用户的问题或指令
推理阶段：分析问题，决定是否需要调用工具
行动阶段：如果需要，调用相应的工具获取信息
整合结果：将工具返回的信息与原有知识结合
生成回答：给出最终的答案
循环执行：如果问题复杂，可能需要多次"推理-行动"循环

Eino框架中，通过react包提供ReAct模式Agent实现的封装：
```go
func NewAgent(ctx context.Context, config *AgentConfig) (_ *Agent, err error) {
    ...
}
```

配置：
```go
type AgentConfig struct {
	// 工具调用chatModel
	ToolCallingModel model.ToolCallingChatModel

	// 工具节点
	ToolsConfig compose.ToolsNodeConfig

	// 调用ChatModel之前做提示词修改,一般用于插入上下文，动态添加系统提示词等
	MessageModifier MessageModifier

	// 最大步数，防止陷入死循环。默认12
	MaxStep int `json:"max_step"`
	//直接返回结果的工具列表，直接返回工具结果，不会进行下一步思考
	ToolReturnDirectly map[string]struct{}

	// 自定义流式输出中，是否包含了工具调用信息
	StreamToolCallChecker func(ctx context.Context, modelOutput *schema.StreamReader[*schema.Message]) (bool, error)

	//  底层是一个Graph，可以设置一个Graph名称
	GraphName string
    //模型节点名称 默认ChatModel
    ModelNodeName string
	// 工具节点名称 默认Tools
	ToolsNodeName string
}
```

# Multi-Agent
当任务变得复杂时，单一Agent可能难以胜任。Multi-Agent系统通过多个专门的Agent协作来解决复杂问题。

Host Multi-Agent采用"主控-专家"模式：

Host Agent：负责理解用户意图，决定将任务分配给哪个专家
Specialist Agents：专门处理特定类型任务的专家Agent

在multiagent/host包下面：
```go
func NewMultiAgent(ctx context.C、、。ontext, config *MultiAgentConfig) (*MultiAgent, error) {
    ....
}
```

配置:
```go
type MultiAgentConfig struct {
	Host        Host // 主控Agent
	Specialists []*Specialist //专家Agent

	Name         string // the name of the host multi-agent
	HostNodeName string // 主控节点名称 默认 "host"
	//流式输出中的工具调用检查器 判断流式输出中是否存在工具调用
	StreamToolCallChecker func(ctx context.Context, modelOutput *schema.StreamReader[*schema.Message]) (bool, error)

	// 汇总Agent，将多个专家agent的结果整合提炼，总结成一份最终报告
	Summarizer *Summarizer
}
```