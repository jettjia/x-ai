package main

import (
	"context"
	"fmt"

	"github.com/cloudwego/eino-ext/a2a/client"
	"github.com/cloudwego/eino-ext/a2a/extension/eino"
	"github.com/cloudwego/eino-ext/a2a/transport/jsonrpc"
	"github.com/cloudwego/eino/adk"
	"github.com/cloudwego/eino/schema"
)

func main() {
	ctx := context.Background()
	t, err := jsonrpc.NewTransport(ctx, &jsonrpc.ClientConfig{
		BaseURL:     "http://127.0.0.1:8888",
		HandlerPath: "/a2a",
	})
	if err != nil {
		panic(err)
	}
	aClient, err := client.NewA2AClient(ctx, &client.Config{
		Transport: t,
	})
	if err != nil {
		panic(err)
	}
	streaming := true
	a, err := eino.NewAgent(ctx, eino.AgentConfig{
		Client:    aClient,
		Streaming: &streaming,
	})
	if err != nil {
		panic(err)
	}
	runner := adk.NewRunner(ctx, adk.RunnerConfig{
		Agent:           a,
		EnableStreaming: true,
	})
	run := runner.Run(ctx, []adk.Message{
		schema.UserMessage("recommend a fiction book to me"),
	})
	for {
		next, b := run.Next()
		if !b {
			break
		}
		printEvent(next)
	}
}

func printEvent(event *adk.AgentEvent) {

	fmt.Printf("name: %s\npath: %s \n", event.AgentName, event.RunPath)
	fmt.Printf("output: %v\n", event.Output.MessageOutput.Message.Content)
}
