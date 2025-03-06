package main

import (
	"io"
	"log"

	"github.com/cloudwego/eino/schema"
)

func reportStream(sr *schema.StreamReader[*schema.Message]) {
	defer sr.Close()

	i := 0
	for {
		message, err := sr.Recv()
		if err == io.EOF {
			return
		}
		if err != nil {
			log.Fatalf("recv failed: %v", err)
		}
		log.Printf("message[%d]: %+v\n", i, message)
		i++
	}
}
