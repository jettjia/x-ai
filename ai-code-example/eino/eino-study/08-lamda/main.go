package main

import (
	"context"
	"errors"
	"fmt"
	"log"

	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"
)

// 定义输入和输出类型
type InputMessage struct {
	Content string
}

type OutputMessage struct {
	Content string
}

func main() {
	// 创建上下文
	ctx := context.Background()

	// 1. 创建Lambda节点：将输入消息转换为大写
	upperCaseLambda := compose.TransformableLambda[*InputMessage, *OutputMessage](func(ctx context.Context, input *schema.StreamReader[*InputMessage]) (output *schema.StreamReader[*OutputMessage], err error) {
		return schema.StreamReaderWithConvert(input, func(input *InputMessage) (output *OutputMessage, err error) {
			if input == nil || input.Content == "" {
				return nil, errors.New("input message is empty")
			}

			// 将输入内容转换为大写
			content := input.Content
			upperContent := ""
			for _, c := range content {
				if c >= 'a' && c <= 'z' {
					upperContent += string(c - 'a' + 'A')
				} else {
					upperContent += string(c)
				}
			}

			return &OutputMessage{
				Content: upperContent,
			}, nil
		}), nil
	})

	// 2. 创建Lambda节点：在转换后的消息前添加前缀
	addPrefixLambda := compose.TransformableLambda[*OutputMessage, *OutputMessage](func(ctx context.Context, input *schema.StreamReader[*OutputMessage]) (output *schema.StreamReader[*OutputMessage], err error) {
		return schema.StreamReaderWithConvert(input, func(input *OutputMessage) (output *OutputMessage, err error) {
			if input == nil || input.Content == "" {
				return nil, errors.New("input message is empty")
			}

			return &OutputMessage{
				Content: "[PROCESSED] " + input.Content,
			}, nil
		}), nil
	})

	// 3. 创建Graph编排
	const (
		upperCaseNodeKey = "upper_case_lambda"
		addPrefixNodeKey = "add_prefix_lambda"
	)

	// 创建Graph
	graph := compose.NewGraph[*InputMessage, *OutputMessage]()

	// 添加节点
	_ = graph.AddLambdaNode(upperCaseNodeKey, upperCaseLambda)
	_ = graph.AddLambdaNode(addPrefixNodeKey, addPrefixLambda)

	// 添加边
	_ = graph.AddEdge(compose.START, upperCaseNodeKey)
	_ = graph.AddEdge(upperCaseNodeKey, addPrefixNodeKey)
	_ = graph.AddEdge(addPrefixNodeKey, compose.END)

	// 编译Graph
	compiledGraph, err := graph.Compile(ctx)
	if err != nil {
		log.Fatalf("Failed to compile graph: %v", err)
	}

	// 4. 测试运行
	testCases := []string{
		"hello eino lambda",
		"go ai development",
		"cloudwego eino framework",
	}

	for _, testInput := range testCases {
		// 创建输入消息
		input := &InputMessage{
			Content: testInput,
		}

		// 运行Graph
		result, err := compiledGraph.Invoke(ctx, input)
		if err != nil {
			log.Fatalf("Failed to invoke graph: %v", err)
		}

		// 输出结果
		fmt.Printf("Input:  %s\n", testInput)
		fmt.Printf("Output: %s\n", result.Content)
		fmt.Println()
	}
}
