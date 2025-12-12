## Eino ADK DeepAgents 示例：Excel 智能体

### 描述
Excel Agent是一个"能理解Excel的智能助手"。它首先将问题分解为步骤，然后逐步执行并验证结果。它可以理解用户问题和上传的文件内容，提出可行的解决方案，并选择适当的工具（系统命令、生成和运行Python代码、网络查询等）来完成任务。

使用之前，您需要进行一些配置：

### 环境变量
```
//（必填）基本LLM模型配置，当前支持Ark和OpenAI模型。
// Ark模型配置
export ARK_API_KEY=""   //（必填）Ark模型API密钥
export ARK_MODEL=""     //（必填）Ark模型名称
export ARK_BASE_URL=""  //（可选）Ark模型基础URL
export ARK_REGION=""    //（可选）Ark模型区域

// OpenAI模型配置
export OPENAI_API_KEY=""       //（必填）OpenAI模型API密钥
export OPENAI_MODEL=""         //（必填）OpenAI模型名称
export OPENAI_BASE_URL=""      //（可选）OpenAI基础URL
export OPENAI_BY_AZURE="false" //（可选）OpenAI是否使用Azure服务

//（可选）Python可执行文件路径，默认使用系统Python。
// 建议使用虚拟环境(venv)，并在启动此智能体之前安装pandas / numpy / matplotlib / openpyxl。
// 当CodeAgent编写的代码因缺少依赖而运行失败时，可能会尝试使用pip命令安装依赖。
// 此时，如果您使用系统环境中的Python，可能会被阻止，导致Excel Agent无法运行并退出。
export EXCEL_AGENT_PYTHON_EXECUTABLE_PATH="python"

//（可选）视觉模型配置，默认null，ReportAgent中的ImagepReader工具将不会激活。
export ARK_VISION_API_KEY=""    // Ark视觉模型API密钥
export ARK_VISION_MODEL=""      // Ark视觉模型名称
export ARK_VISION_BASE_URL=""   // Ark视觉模型基础URL
export ARK_VISION_REGION=""     // Ark视觉模型区域
```

### 输入
Excel Agent的输入是用户需求描述和一系列待处理文件：
- `main.go`中的第一行表示用户输入的需求描述：
  ```
    func main() {
        // query := schema.UserMessage("Count the recommended novel names and recommended times in the attachment file, and write the results to the file. The content with "" is the name of the novel and forms a table. The header is the name of the novel and the number of recommendations. The novels with the same name are listed in only one line, and the number of recommendations is added")
        // query := schema.UserMessage("Read the content in simulated question. csv, put the question, answer, resolution and options in the same line in a standardized format, and simply write the answer to the resolution")
        query := schema.UserMessage("Please help me extract the first column in question.csv table into a new csv")
    }
  ```
- `adk/multiagent/deep/playground/input`是默认的附件输入路径。例如，上述查询中提到的`question.csv`文件需要放在此目录下才能被智能体读取。此外，它支持配置环境变量`EXCEL_AGENT_INPUT_DIR`来设置附件输入路径（绝对路径）。
- 路径`adk/multiagent/deep/playground/test_data`中提供了几个示例文件供您测试：
  ```
    % tree adk/multiagent/deep/playground/test_data
    adk/multiagent/deep/playground/test_data
    ├── questions.csv
    ├── 推荐小说.txt
    └── 模拟出题.csv

    1 directory, 3 files
  ```

### 输出
默认工作目录为`adk/multiagent/deep/playground/${uuid}`。

您可以通过设置环境变量来自定义工作目录：`export EXCEL_AGENT_WORK_DIR="your_path"`（`/$uuid`前的绝对路径）。