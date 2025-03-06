package main

import (
	"fmt"
	"testing"
)

// go test -v -run Test_createMessagesFromTemplate ./
func Test_createMessagesFromTemplate(t *testing.T) {
	messages := createMessagesFromTemplate()
	fmt.Printf("formatted message: %v", messages)
}
