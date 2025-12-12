package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"github.com/cloudwego/eino/adk"

	"github.com/cloudwego/eino-examples/adk/common/prints"
	"github.com/cloudwego/eino-examples/adk/common/trace"
)

func main() {
	ctx := context.Background()

	traceCloseFn, startSpanFn := trace.AppendCozeLoopCallbackIfConfigured(ctx)
	defer traceCloseFn(ctx)

	sv, err := buildSupervisor(ctx)
	if err != nil {
		log.Fatalf("build supervisor failed: %v", err)
	}

	query := "计算2024年美国和纽约州的国内生产总值。纽约州占美国GDP的百分比是多少？"

	runner := adk.NewRunner(ctx, adk.RunnerConfig{
		Agent:           sv,
		EnableStreaming: true,
	})

	ctx, endSpanFn := startSpanFn(ctx, "Supervisor", query)

	iter := runner.Query(ctx, query)

	fmt.Println("\nuser query: ", query)

	var lastMessage adk.Message
	for {
		event, hasEvent := iter.Next()
		if !hasEvent {
			break
		}

		prints.Event(event)

		if event.Output != nil {
			lastMessage, _, err = adk.GetMessage(event)
		}
	}

	endSpanFn(ctx, lastMessage)

	// wait for all span to be ended
	time.Sleep(5 * time.Second)
}
