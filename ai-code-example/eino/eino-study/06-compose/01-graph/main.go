package main

import (
	"context"
	"errors"
	"log"
	"os"

	"github.com/cloudwego/eino-ext/components/model/openai"
	"github.com/cloudwego/eino/components/prompt"
	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/components/tool/utils"
	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"
)

type userInfoRequest struct {
	Email string `json:"email"`
	Name  string `json:"name"`
}
type userInfoResponse struct {
	Name     string `json:"name"`
	Email    string `json:"email"`
	Company  string `json:"company"`
	Position string `json:"position"`
	Salary   string `json:"salary"`
}

func main() {
	ctx := context.Background()
	g := compose.NewGraph[map[string]any, *schema.Message]()
	//1. 创建ChatTemplate节点
	systemTpl := `你是一名房产经纪人，结合用户的薪酬和工作，使用 user_info API，为其提供相关的房产信息。邮箱是必须的`
	chatTpl := prompt.FromMessages(schema.FString,
		schema.SystemMessage(systemTpl),
		schema.MessagesPlaceholder("histories", true),
		schema.UserMessage("{user_query}"))
	recommendTpl := `
		你是一名房产经纪人，结合工具提供的用户信息，推荐房产
			--- 房产信息 ---

		### A. 楼盘列表

		**1. 瀚海星辰 (ID: A-01)**
		- **区域**: 海淀区-中关村
		- **特点**: 顶级学区房, 毗邻多所名校, 周围遍布知名科技公司（如字节跳动、腾讯等）。
		- **户型**: 120平米三居室
		- **总价**: 约1500万人民币
		- **适合人群**: 科技公司高管、重视子女教育的家庭。

		**2. 国贸天际 (ID: B-02)**
		- **区域**: 朝阳区-国贸CBD
		- **特点**: 城市核心地标, 270度落地窗俯瞰CBD夜景, 奢华精装修，顶级商业配套。
		- **户型**: 280平米大平层
		- **总价**: 约3500万人民币
		- **适合人群**: 企业家、公司创始人(CEO/C-level)、金融精英、追求顶级生活品质人士。

		**3. 未来之城 (ID: C-03)**
		- **区域**: 通州区-城市副中心
		- **特点**: 新兴规划区域, 潜力巨大, 环境优美, 配套设施完善, 性价比高。
		- **户型**: 140平米四居室
		- **总价**: 约800万人民币
		- **适合人群**: 在国贸或副中心工作的白领、首次改善型购房家庭。

		**4. 文艺 loft (ID: D-04)**
		- **区域**: 朝阳区-798艺术区
		- **特点**: 设计师风格, 挑高5米, 充满艺术气息, 交通便利。
		- **户型**: 60平米复式Loft
		- **总价**: 约450万人民币
		- **适合人群**: 年轻单身贵族、设计师、创意工作者。

		### B. 购房建议规则

		1.  **预算评估**:
			- 房屋总价建议不超过家庭年收入的10倍。
			- 月供（按30年商业贷款，利率4%估算）不应超过家庭月收入的50%。
		2.  **职住平衡**: 推荐的房产区域应与用户公司所在地有较好的通勤关系。例如，在字节跳动工作的高管，优先推荐海淀区的“瀚海星辰”。
		3.  **身份匹配**: 房产的“适合人群”标签应与用户的职位和身份高度匹配。例如，CEO身份的用户应优先考虑“国贸天际”这类彰显身份的豪宅。

	`
	//2. 创建chatModel节点
	chatModel, err := openai.NewChatModel(ctx, &openai.ChatModelConfig{
		APIKey:  os.Getenv("OPENAI_API_KEY"),
		Model:   os.Getenv("OPENAI_MODEL"),
		BaseURL: os.Getenv("OPENAI_BASE_URL"),
		ByAzure: func() bool {
			return os.Getenv("OPENAI_BY_AZURE") == "true"
		}(),
	})
	if err != nil {
		log.Fatal(err)
	}
	//3. 创建工具节点
	userInfoTool := utils.NewTool(
		&schema.ToolInfo{
			Name: "user_info",
			Desc: "根据用户的姓名和邮箱，查询用户的公司、职位、薪酬信息",
			ParamsOneOf: schema.NewParamsOneOfByParams(map[string]*schema.ParameterInfo{
				"name": {
					Type: "string",
					Desc: "用户的姓名",
				},
				"email": {
					Type: "string",
					Desc: "用户的邮箱",
				},
			}),
		}, func(ctx context.Context, input *userInfoRequest) (output *userInfoResponse, err error) {
			return &userInfoResponse{
				Name:     input.Name,
				Email:    input.Email,
				Company:  "Bytedance",
				Position: "高级工程师",
				Salary:   "60000",
			}, nil
		})
	//4. 绑定工具到模型
	info, err := userInfoTool.Info(ctx)
	if err != nil {
		panic(err)
	}
	err = chatModel.BindTools([]*schema.ToolInfo{info})
	if err != nil {
		panic(err)
	}
	//5. 创建工具节点
	toolsNode, err := compose.NewToolNode(ctx, &compose.ToolsNodeConfig{
		Tools: []tool.BaseTool{userInfoTool},
	})
	if err != nil {
		panic(err)
	}
	//6. 创建转换lambda节点
	transformOps := func(ctx context.Context, input *schema.StreamReader[[]*schema.Message]) (output *schema.StreamReader[*schema.Message], err error) {
		return schema.StreamReaderWithConvert(input, func(input []*schema.Message) (output *schema.Message, err error) {
			if len(input) > 0 {
				return input[0], nil
			}
			return nil, errors.New("no message")
		}), nil
	}
	lambda := compose.TransformableLambda[[]*schema.Message, *schema.Message](transformOps)
	//7. 创建转换lambda节点 给下一个chatmodel构建提示词
	promptTransformOps := func(ctx context.Context, input *schema.StreamReader[*schema.Message]) (output *schema.StreamReader[[]*schema.Message], err error) {
		return schema.StreamReaderWithConvert(input, func(input *schema.Message) (output []*schema.Message, err error) {
			var messages []*schema.Message
			messages = append(messages, schema.SystemMessage(recommendTpl), input)
			return messages, nil
		}), nil
	}
	lambdaPrompt := compose.TransformableLambda[*schema.Message, []*schema.Message](promptTransformOps)
	//8. 创建Graph编排
	const (
		promptNodeKey        = "prompt"
		chatNodeKey          = "chat"
		toolsNodeKey         = "tools"
		recommendChatNodeKey = "chat_recommend"
		lambdaNodeKey        = "lambda"
		lambdaPromptNodeKey  = "lambdaPrompt"
	)
	//9. 添加节点
	_ = g.AddChatTemplateNode(promptNodeKey, chatTpl)
	_ = g.AddChatModelNode(chatNodeKey, chatModel)
	_ = g.AddToolsNode(toolsNodeKey, toolsNode)
	_ = g.AddChatModelNode(recommendChatNodeKey, chatModel)
	_ = g.AddLambdaNode(lambdaNodeKey, lambda)
	_ = g.AddLambdaNode(lambdaPromptNodeKey, lambdaPrompt)
	//10. 添加边 也就是节点之间的依赖关系
	_ = g.AddEdge(compose.START, promptNodeKey)
	_ = g.AddEdge(promptNodeKey, chatNodeKey)
	_ = g.AddEdge(chatNodeKey, toolsNodeKey)
	_ = g.AddEdge(toolsNodeKey, lambdaNodeKey)
	_ = g.AddEdge(lambdaNodeKey, lambdaPromptNodeKey)
	_ = g.AddEdge(lambdaPromptNodeKey, recommendChatNodeKey)
	_ = g.AddEdge(recommendChatNodeKey, compose.END)
	//11. 编译运行
	runnable, err := g.Compile(ctx)
	if err != nil {
		panic(err)
	}
	output, err := runnable.Invoke(ctx, map[string]any{
		"histories":  []*schema.Message{},
		"user_query": "我叫 zhangsan, 邮箱是 zhangsan@bytedance.com, 帮我推荐一处房产",
	})
	if err != nil {
		panic(err)
	}
	println("=====================思考内容====================")
	if output.ReasoningContent != "" {
		println(output.ReasoningContent)
	}
	println("=========================================")
	if output.Content != "" {
		println(output.Content)
	}
}
