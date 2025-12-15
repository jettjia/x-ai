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

func main() {
	ctx := context.Background()

	// 创建Workflow编排
	wf := compose.NewWorkflow[map[string]any, *schema.Message]()

	// 1. 创建系统提示词模板
	systemTpl := `你是一名房产经纪人，结合用户的薪酬和工作，使用 user_info API，为其提供相关的房产信息。邮箱是必须的`
	chatTpl := prompt.FromMessages(schema.FString,
		schema.SystemMessage(systemTpl),
		schema.MessagesPlaceholder("histories", true),
		schema.UserMessage("{user_query}"))

	// 2. 创建推荐模板
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
2.  **职住平衡**: 推荐的房产区域应与用户公司所在地有较好的通勤关系。例如，在字节跳动工作的高管，优先推荐海淀区的"瀚海星辰"。
3.  **身份匹配**: 房产的"适合人群"标签应与用户的职位和身份高度匹配。例如，CEO身份的用户应优先考虑"国贸天际"这类彰显身份的豪宅。
`

	// 3. 创建chatModel
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

	// 4. 创建工具
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

	// 5. 绑定工具到模型
	info, err := userInfoTool.Info(ctx)
	if err != nil {
		panic(err)
	}
	err = chatModel.BindTools([]*schema.ToolInfo{info})
	if err != nil {
		panic(err)
	}

	// 6. 创建工具节点
	toolsNode, err := compose.NewToolNode(ctx, &compose.ToolsNodeConfig{
		Tools: []tool.BaseTool{userInfoTool},
	})
	if err != nil {
		panic(err)
	}

	// 7. 创建转换函数，将 []*schema.Message 转换为 *schema.Message
	transformOps := func(ctx context.Context, input *schema.StreamReader[[]*schema.Message]) (output *schema.StreamReader[*schema.Message], err error) {
		return schema.StreamReaderWithConvert(input, func(input []*schema.Message) (output *schema.Message, err error) {
			if len(input) > 0 {
				return input[0], nil
			}
			return nil, errors.New("no message")
		}), nil
	}
	lambda := compose.TransformableLambda[[]*schema.Message, *schema.Message](transformOps)
	// 8. 创建另一个转换函数，将 *schema.Message 转换为 []*schema.Message
	promptTransformOps := func(ctx context.Context, input *schema.StreamReader[*schema.Message]) (output *schema.StreamReader[[]*schema.Message], err error) {
		return schema.StreamReaderWithConvert(input, func(input *schema.Message) (output []*schema.Message, err error) {
			var messages []*schema.Message
			messages = append(messages, schema.SystemMessage(recommendTpl), input)
			return messages, nil
		}), nil
	}
	lambdaPrompt := compose.TransformableLambda[*schema.Message, []*schema.Message](promptTransformOps)

	// 9. 添加节点到Workflow
	// 添加聊天模板节点
	wf.AddChatTemplateNode("prompt", chatTpl).AddInput(compose.START)

	// 添加第一个聊天模型节点
	wf.AddChatModelNode("chat", chatModel).AddInput("prompt")

	// 添加工具节点
	wf.AddToolsNode("tools", toolsNode).AddInput("chat")

	// 添加转换节点（将[]*schema.Message转换为*schema.Message）
	wf.AddLambdaNode("transform", lambda).AddInput("tools")

	// 添加转换节点（将*schema.Message转换为[]*schema.Message）
	wf.AddLambdaNode("prompt_transform", lambdaPrompt).AddInput("transform")

	// 添加第二个聊天模型节点
	wf.AddChatModelNode("chat_recommend", chatModel).AddInput("prompt_transform")

	// 从chat_recommend到END节点
	wf.End().AddInput("chat_recommend")

	// 11. 编译Workflow
	runnable, err := wf.Compile(ctx)
	if err != nil {
		panic(err)
	}

	// 12. 执行调用
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

type userInfoRequest struct {
	Name  string `json:"name"`
	Email string `json:"email"`
}

type userInfoResponse struct {
	Name     string `json:"name"`
	Email    string `json:"email"`
	Company  string `json:"company"`
	Position string `json:"position"`
	Salary   string `json:"salary"`
}
