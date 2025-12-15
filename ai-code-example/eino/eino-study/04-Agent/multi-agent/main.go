package main

import (
	"context"
	"fmt"
	"io"
	"os"
	"strings"

	"github.com/cloudwego/eino-ext/components/model/openai"
	"github.com/cloudwego/eino/flow/agent"
	"github.com/cloudwego/eino/flow/agent/multiagent/host"
	"github.com/cloudwego/eino/schema"
)

// 创建Host Agent
func newHost(ctx context.Context) (*host.Host, error) {
	// 初始化模型
	chatModel, err := openai.NewChatModel(ctx, &openai.ChatModelConfig{
		APIKey:  os.Getenv("OPENAI_API_KEY"),
		Model:   os.Getenv("OPENAI_MODEL"),
		BaseURL: os.Getenv("OPENAI_BASE_URL"),
		ByAzure: func() bool {
			return os.Getenv("OPENAI_BY_AZURE") == "true"
		}(),
	})
	if err != nil {
		return nil, err
	}
	return &host.Host{
		ToolCallingModel: chatModel,
		SystemPrompt:     "你是一个日记助手，可以帮助用户写日记、读日记。当用户要求查看日记内容时，必须调用view_journal_content工具。当用户要求写日记时，必须调用write_journal工具。",
	}, nil
}

// 创建写日记专家
func newWriteJournalSpecialist(ctx context.Context) (*host.Specialist, error) {
	// 初始化模型
	chatModel, err := openai.NewChatModel(ctx, &openai.ChatModelConfig{
		APIKey:  os.Getenv("OPENAI_API_KEY"),
		Model:   os.Getenv("OPENAI_MODEL"),
		BaseURL: os.Getenv("OPENAI_BASE_URL"),
		ByAzure: func() bool {
			return os.Getenv("OPENAI_BY_AZURE") == "true"
		}(),
	})
	if err != nil {
		return nil, err
	}
	return &host.Specialist{
		ChatModel:    chatModel,
		SystemPrompt: "请将用户输入的内容写入日记。请勿返回任何内容。",
		AgentMeta: host.AgentMeta{
			Name:        "write_journal",
			IntendedUse: "将用户输入的内容写入日记",
		},
		Invokable: func(ctx context.Context, input []*schema.Message, opts ...agent.AgentOption) (*schema.Message, error) {
			return &schema.Message{
				Role:    schema.Assistant,
				Content: "日记已保存",
			}, nil
		},
		Streamable: func(ctx context.Context, input []*schema.Message, opts ...agent.AgentOption) (*schema.StreamReader[*schema.Message], error) {
			return &schema.StreamReader[*schema.Message]{}, nil
		},
	}, nil
}

// 创建读日记专家
func newReadJournalSpecialist(ctx context.Context) (*host.Specialist, error) {
	// 初始化模型
	chatModel, err := openai.NewChatModel(ctx, &openai.ChatModelConfig{
		APIKey:  os.Getenv("OPENAI_API_KEY"),
		Model:   os.Getenv("OPENAI_MODEL"),
		BaseURL: os.Getenv("OPENAI_BASE_URL"),
		ByAzure: func() bool {
			return os.Getenv("OPENAI_BY_AZURE") == "true"
		}(),
	})
	if err != nil {
		return nil, err
	}
	return &host.Specialist{
		ChatModel:    chatModel,
		SystemPrompt: "请将日记内容返回给用户。",
		AgentMeta: host.AgentMeta{
			Name:        "view_journal_content",
			IntendedUse: "读取并显示日记内容",
		},
		Invokable: func(ctx context.Context, input []*schema.Message, opts ...agent.AgentOption) (*schema.Message, error) {
			// 从readJournal函数获取实际内容
			journal, err := readJournal()
			if err != nil {
				return nil, err
			}
			content, err := io.ReadAll(journal)
			if err != nil {
				return nil, err
			}
			return &schema.Message{
				Role:    schema.Assistant,
				Content: string(content),
			}, nil
		},
	}, nil
}

// 模拟读取日记的函数
func readJournal() (io.Reader, error) {
	// 实际应用中这里会从文件或数据库读取内容
	content := "今天天气很好\n学习了Eino框架\n创建了一个Multi-Agent系统\n"
	return strings.NewReader(content), nil
}

func main() {
	ctx := context.Background()
	// 创建Host和专家Agents
	h, err := newHost(ctx)
	if err != nil {
		panic(err)
	}

	writer, err := newWriteJournalSpecialist(ctx)
	if err != nil {
		panic(err)
	}

	reader, err := newReadJournalSpecialist(ctx)
	if err != nil {
		panic(err)
	}

	// 创建Multi-Agent系统
	hostMA, err := host.NewMultiAgent(ctx, &host.MultiAgentConfig{
		Host: *h,
		Specialists: []*host.Specialist{
			writer,
			reader,
		},
	})
	if err != nil {
		panic(err)
	}

	// 交互式使用示例
	fmt.Println("=== 日记助手 ===")

	// 先写日记
	msg := &schema.Message{
		Role:    schema.User,
		Content: "写日志，今天学习了eino框架的multiagent",
	}

	out, err := hostMA.Generate(ctx, []*schema.Message{msg})
	if err != nil {
		fmt.Printf("错误: %v\n", err)
	}

	fmt.Print("助手: ")
	fmt.Println(out.Content)

	// 然后读日记
	msg2 := []*schema.Message{
		{
			Role:    schema.User,
			Content: "读取日记内容",
		},
	}
	out2, err := hostMA.Generate(ctx, msg2)
	if err != nil {
		fmt.Printf("错误: %v\n", err)
	}

	fmt.Print("助手2: ")
	fmt.Println(out2.Content)
}
