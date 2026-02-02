package example01

import (
	"context"

	"github.com/cloudwego/eino/components/prompt"
	"github.com/cloudwego/eino/schema"
)

type ChatTemplateConfig struct {
	FormatType schema.FormatType
	Templates  []schema.MessagesTemplate
}

func newChatTemplate(ctx context.Context) (ctp prompt.ChatTemplate, err error) {
	config := &ChatTemplateConfig{schema.FString, []schema.MessagesTemplate{
		schema.SystemMessage("你是一个{role}"),
		&schema.Message{
			Role:    schema.User,
			Content: "完成{task}。",
		},
	}}
	ctp = prompt.FromMessages(config.FormatType, config.Templates...)
	return ctp, nil
}
