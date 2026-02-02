package main

import (
	"context"
	"log"
	"os"
	"os/signal"
	"syscall"

	"github.com/jettjia/ai-code-example/eino/eino-dev/example-01"

	"github.com/cloudwego/eino-ext/devops"
)

func main() {
	ctx := context.Background()

	// Init eino devops server
	err := devops.Init(ctx)
	if err != nil {
		log.Printf("[eino dev] init failed, err=%v", err)
		return
	}

	// Register chain, graph and state_graph for demo use
	_, err = example01.Buildtest(ctx)
	if err != nil {
		log.Printf("[eino dev] build tt failed, err=%v", err)
		return
	}

	// Blocking process exits
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)
	<-sigs

	// Exit
	log.Printf("[eino dev] shutting down\n")

}
