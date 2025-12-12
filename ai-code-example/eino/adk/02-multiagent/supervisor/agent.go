package main

import (
	"context"
	"fmt"

	"github.com/cloudwego/eino/adk"
	"github.com/cloudwego/eino/adk/prebuilt/supervisor"
	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/compose"

	"github.com/cloudwego/eino-examples/adk/common/model"
	"github.com/cloudwego/eino-examples/flow/agent/multiagent/plan_execute/tools"
)

func buildSearchAgent(ctx context.Context) (adk.Agent, error) {
	m := model.NewChatModel()

	type searchReq struct {
		Query string `json:"query"`
	}

	type searchResp struct {
		Result string `json:"result"`
	}

	// 模拟搜索函数
	search := func(ctx context.Context, req *searchReq) (*searchResp, error) {
		return &searchResp{
			Result: "2024年，美国GDP为29.18万亿美元，纽约州GDP为2.297万亿美元",
		}, nil
	}

	searchTool, err := tools.SafeInferTool("search", "search the internet for info", search)
	if err != nil {
		return nil, err
	}

	return adk.NewChatModelAgent(ctx, &adk.ChatModelAgentConfig{
		Name:        "research_agent",
		Description: "负责在互联网上搜索信息的代理",
		Instruction: `
		You are a research agent.


        指令:
        - 仅负责研究相关任务，不进行任何数学计算
        - 不估计任何数字
        - 完成任务后，直接向监督者报告结果
        - 仅返回工作结果，不包含任何其他文本`,
		Model: m,
		ToolsConfig: adk.ToolsConfig{
			ToolsNodeConfig: compose.ToolsNodeConfig{
				Tools: []tool.BaseTool{searchTool},
				UnknownToolsHandler: func(ctx context.Context, name, input string) (string, error) {
					return fmt.Sprintf("unknown tool: %s", name), nil
				},
			},
		},
	})
}

func buildMathAgent(ctx context.Context) (adk.Agent, error) {
	m := model.NewChatModel()

	type addReq struct {
		A float64 `json:"a"`
		B float64 `json:"b"`
	}

	type addResp struct {
		Result float64
	}

	add := func(ctx context.Context, req *addReq) (*addResp, error) {
		return &addResp{
			Result: req.A + req.B,
		}, nil
	}

	addTool, err := tools.SafeInferTool("add", "add two numbers", add)
	if err != nil {
		return nil, err
	}

	type multiplyReq struct {
		A float64 `json:"a"`
		B float64 `json:"b"`
	}

	type multiplyResp struct {
		Result float64
	}

	multiply := func(ctx context.Context, req *multiplyReq) (*multiplyResp, error) {
		return &multiplyResp{
			Result: req.A * req.B,
		}, nil
	}

	multiplyTool, err := tools.SafeInferTool("multiply", "multiply two numbers", multiply)
	if err != nil {
		return nil, err
	}

	type divideReq struct {
		A float64 `json:"a"`
		B float64 `json:"b"`
	}

	type divideResp struct {
		Result float64
	}

	divide := func(ctx context.Context, req *divideReq) (*divideResp, error) {
		return &divideResp{
			Result: req.A / req.B,
		}, nil
	}

	divideTool, err := tools.SafeInferTool("divide", "divide two numbers", divide)
	if err != nil {
		return nil, err
	}
	return adk.NewChatModelAgent(ctx, &adk.ChatModelAgentConfig{
		Name:        "math_agent",
		Description: "the agent responsible to do math",
		Instruction: `
		You are a math agent.


        INSTRUCTIONS:
        - Assist ONLY with math-related tasks
        - After you're done with your tasks, respond to the supervisor directly
        - Respond ONLY with the results of your work, do NOT include ANY other text.`,
		Model: m,
		ToolsConfig: adk.ToolsConfig{
			ToolsNodeConfig: compose.ToolsNodeConfig{
				Tools: []tool.BaseTool{addTool, multiplyTool, divideTool},
				UnknownToolsHandler: func(ctx context.Context, name, input string) (string, error) {
					return fmt.Sprintf("unknown tool: %s", name), nil
				},
			},
		},
	})
}

func buildSupervisor(ctx context.Context) (adk.Agent, error) {
	m := model.NewChatModel()

	sv, err := adk.NewChatModelAgent(ctx, &adk.ChatModelAgentConfig{
		Name:        "supervisor",
		Description: "the agent responsible to supervise tasks",
		Instruction: `
		You are a supervisor managing two agents:

        - a research agent. Assign research-related tasks to this agent
        - a math agent. Assign math-related tasks to this agent
        Assign work to one agent at a time, do not call agents in parallel.
        Do not do any work yourself.`,
		Model: m,
		Exit:  &adk.ExitTool{},
	})
	if err != nil {
		return nil, err
	}

	searchAgent, err := buildSearchAgent(ctx)
	if err != nil {
		return nil, err
	}
	mathAgent, err := buildMathAgent(ctx)
	if err != nil {
		return nil, err
	}

	return supervisor.New(ctx, &supervisor.Config{
		Supervisor: sv,
		SubAgents:  []adk.Agent{searchAgent, mathAgent},
	})
}
