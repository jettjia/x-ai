什么是 Eino ADK
Eino ADK 参考 Google-ADK 的设计，提供了 Go 语言 的 Agents 开发的灵活组合框架，即 Agent、Multi-Agent 开发框架，并为多 Agent 交互场景沉淀了通用的上下文传递、事件流分发和转换、任务控制权转让、中断与恢复、通用切面等能力。

什么是 Agent
Agent 是 Eino ADK 的核心，它代表一个独立的、可执行的智能任务单元。你可以把它想象成一个能够理解指令、执行任务并给出回应的“智能体”。每个 Agent 都有明确的名称和描述，使其可以被其他 Agent 发现和调用。

任何需要与大语言模型（LLM）交互的场景都可以抽象为一个 Agent。例如：

一个用于查询天气信息的 Agent。
一个用于预定会议的 Agent。
一个能够回答特定领域知识的 Agent。
Eino ADK 中的 Agent
Eino ADK 中的所有功能设计均围绕 Agent 抽象设计展开：
```go
type Agent interface {
    Name(ctx context.Context) string
    Description(ctx context.Context) string
    Run(ctx context.Context, input *AgentInput) *AsyncIterator[*AgentEvent]
}
```