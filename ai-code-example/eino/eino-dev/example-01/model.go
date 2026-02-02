package example01

import (
	"context"
	"os"

	"github.com/cloudwego/eino-ext/components/model/openai"
	"github.com/cloudwego/eino/components/model"
)

// newChatModel component initialization function of node 'ChatModel1' in graph 'test'
func newChatModel(ctx context.Context) (cm model.BaseChatModel, err error) {
	// TODO Modify component configuration here.
	config := &openai.ChatModelConfig{
		Model:   os.Getenv("OPENAI_MODEL"),
		APIKey:  os.Getenv("OPENAI_API_KEY"),
		BaseURL: os.Getenv("OPENAI_BASE_URL"),
	}
	cm, err = openai.NewChatModel(ctx, config)
	if err != nil {
		return nil, err
	}
	return cm, nil
}
